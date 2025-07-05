from flask import Blueprint, request, jsonify
from werkzeug.security import generate_password_hash, check_password_hash
import jwt
import datetime
from src.models.database import db, User

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/login', methods=['POST'])
def login():
    try:
        data = request.get_json()
        email = data.get('email')
        password = data.get('password')
        
        if not email or not password:
            return jsonify({'error': 'Email e senha são obrigatórios'}), 400
        
        user = User.query.filter_by(email=email).first()
        
        if not user or not check_password_hash(user.password_hash, password):
            return jsonify({'error': 'Credenciais inválidas'}), 401
        
        # Gerar token JWT
        token = jwt.encode({
            'user_id': user.id,
            'email': user.email,
            'role': user.role.value if hasattr(user.role, 'value') else str(user.role),
            'exp': datetime.datetime.utcnow() + datetime.timedelta(hours=24)
        }, 'mestres_cafe_secret_key_2024', algorithm='HS256')
        
        return jsonify({
            'token': token,
            'user': {
                'id': user.id,
                'email': user.email,
                'name': user.name,
                'role': user.role.value if hasattr(user.role, 'value') else str(user.role),
                'points': user.points,
                'level': user.level,
                'total_spent': float(user.total_spent),
                'account_type': user.account_type
            }
        })
        
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@auth_bp.route('/register', methods=['POST'])
def register():
    try:
        data = request.get_json()
        email = data.get('email')
        password = data.get('password')
        name = data.get('name')
        
        if not email or not password or not name:
            return jsonify({'error': 'Email, senha e nome são obrigatórios'}), 400
        
        # Verificar se usuário já existe
        existing_user = User.query.filter_by(email=email).first()
        if existing_user:
            return jsonify({'error': 'Usuário já existe'}), 400
        
        # Criar novo usuário
        password_hash = generate_password_hash(password)
        new_user = User(
            email=email,
            password_hash=password_hash,
            name=name
        )
        
        db.session.add(new_user)
        db.session.commit()
        
        return jsonify({
            'message': 'Usuário criado com sucesso',
            'user': {
                'id': new_user.id,
                'email': new_user.email,
                'name': new_user.name,
                'role': new_user.role.value if hasattr(new_user.role, 'value') else str(new_user.role)
            }
        }), 201
        
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500

@auth_bp.route('/me', methods=['GET'])
def get_current_user():
    try:
        token = request.headers.get('Authorization')
        if not token:
            return jsonify({'error': 'Token não fornecido'}), 401
        
        # Remover 'Bearer ' do token
        if token.startswith('Bearer '):
            token = token[7:]
        
        decoded = jwt.decode(token, 'mestres_cafe_secret_key_2024', algorithms=['HS256'])
        user = User.query.get(decoded['user_id'])
        
        if not user:
            return jsonify({'error': 'Usuário não encontrado'}), 404
        
        return jsonify({
            'user': {
                'id': user.id,
                'email': user.email,
                'name': user.name,
                'role': user.role.value if hasattr(user.role, 'value') else str(user.role),
                'points': user.points,
                'level': user.level,
                'total_spent': float(user.total_spent),
                'account_type': user.account_type
            }
        })
        
    except jwt.ExpiredSignatureError:
        return jsonify({'error': 'Token expirado'}), 401
    except jwt.InvalidTokenError:
        return jsonify({'error': 'Token inválido'}), 401
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@auth_bp.route('/logout', methods=['POST'])
def logout():
    return jsonify({'message': 'Logout realizado com sucesso'})

