"""
Rotas de depoimentos para a API Mestres do Café
"""

from flask import Blueprint, jsonify, request

# Criar blueprint
testimonials_bp = Blueprint('testimonials', __name__)

# Dados mock para desenvolvimento
MOCK_TESTIMONIALS = [
    {
        'id': '1',
        'name': 'João Silva',
        'email': 'joao@example.com',
        'rating': 5,
        'comment': 'Café excelente! A qualidade é incomparável e o sabor é único.',
        'product_name': 'Café Especial do Brasil',
        'avatar_url': 'https://images.unsplash.com/photo-1507003211169-0a1dd7228f2d?w=100',
        'created_at': '2024-01-15T10:30:00Z',
        'is_featured': True,
        'is_approved': True
    },
    {
        'id': '2',
        'name': 'Maria Santos',
        'email': 'maria@example.com',
        'rating': 5,
        'comment': 'Aroma incrível e torra perfeita. Recomendo a todos os amantes de café!',
        'product_name': 'Café Gourmet Colombiano',
        'avatar_url': 'https://images.unsplash.com/photo-1494790108755-2616b612b786?w=100',
        'created_at': '2024-01-10T14:15:00Z',
        'is_featured': True,
        'is_approved': True
    },
    {
        'id': '3',
        'name': 'Carlos Oliveira',
        'email': 'carlos@example.com',
        'rating': 5,
        'comment': 'O melhor café que já experimentei. Entrega rápida e produto de primeira qualidade.',
        'product_name': 'Café Etíope Natural',
        'avatar_url': 'https://images.unsplash.com/photo-1472099645785-5658abf4ff4e?w=100',
        'created_at': '2024-01-05T09:45:00Z',
        'is_featured': True,
        'is_approved': True
    },
    {
        'id': '4',
        'name': 'Ana Paula',
        'email': 'ana@example.com',
        'rating': 4,
        'comment': 'Café muito bom, sabor equilibrado e preço justo. Voltarei a comprar.',
        'product_name': 'Café Premium Guatemala',
        'avatar_url': 'https://images.unsplash.com/photo-1438761681033-6461ffad8d80?w=100',
        'created_at': '2024-01-03T16:20:00Z',
        'is_featured': False,
        'is_approved': True
    },
    {
        'id': '5',
        'name': 'Pedro Costa',
        'email': 'pedro@example.com',
        'rating': 5,
        'comment': 'Excelente atendimento e produto de qualidade superior. Parabéns!',
        'product_name': 'Café Especial do Brasil',
        'avatar_url': 'https://images.unsplash.com/photo-1500648767791-00dcc994a43e?w=100',
        'created_at': '2024-01-01T11:30:00Z',
        'is_featured': False,
        'is_approved': True
    }
]

@testimonials_bp.route('', methods=['GET'])
def get_all_testimonials():
    """Listar todos os depoimentos aprovados"""
    try:
        approved_testimonials = [t for t in MOCK_TESTIMONIALS if t['is_approved']]
        
        return jsonify({
            'success': True,
            'data': approved_testimonials,
            'total': len(approved_testimonials)
        })
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500

@testimonials_bp.route('/featured', methods=['GET'])
def get_featured_testimonials():
    """Listar depoimentos em destaque"""
    try:
        featured = [t for t in MOCK_TESTIMONIALS if t['is_featured'] and t['is_approved']]
        
        return jsonify({
            'success': True,
            'data': featured,
            'total': len(featured)
        })
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500

@testimonials_bp.route('/<testimonial_id>', methods=['GET'])
def get_testimonial(testimonial_id):
    """Obter depoimento específico"""
    try:
        testimonial = next((t for t in MOCK_TESTIMONIALS if t['id'] == testimonial_id), None)
        if not testimonial:
            return jsonify({
                'success': False,
                'error': 'Depoimento não encontrado'
            }), 404
        
        return jsonify({
            'success': True,
            'data': testimonial
        })
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500

@testimonials_bp.route('', methods=['POST'])
def create_testimonial():
    """Criar novo depoimento"""
    try:
        data = request.get_json()
        
        # Validação básica
        if not data or 'name' not in data or 'comment' not in data or 'rating' not in data:
            return jsonify({
                'success': False,
                'error': 'Nome, comentário e avaliação são obrigatórios'
            }), 400
        
        # Validar rating
        try:
            rating = int(data['rating'])
            if rating < 1 or rating > 5:
                return jsonify({
                    'success': False,
                    'error': 'Avaliação deve ser entre 1 e 5'
                }), 400
        except ValueError:
            return jsonify({
                'success': False,
                'error': 'Avaliação deve ser um número'
            }), 400
        
        # Simular criação do depoimento
        new_testimonial = {
            'id': str(len(MOCK_TESTIMONIALS) + 1),
            'name': data['name'],
            'email': data.get('email', ''),
            'rating': rating,
            'comment': data['comment'],
            'product_name': data.get('product_name', ''),
            'avatar_url': data.get('avatar_url', ''),
            'created_at': '2024-01-20T12:00:00Z',
            'is_featured': False,
            'is_approved': False  # Novos depoimentos precisam ser aprovados
        }
        
        MOCK_TESTIMONIALS.append(new_testimonial)
        
        return jsonify({
            'success': True,
            'data': new_testimonial,
            'message': 'Depoimento criado com sucesso! Aguarde aprovação.'
        }), 201
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500

@testimonials_bp.route('/<testimonial_id>', methods=['PUT'])
def update_testimonial(testimonial_id):
    """Atualizar depoimento"""
    try:
        data = request.get_json()
        
        # Encontrar depoimento
        testimonial_index = next((i for i, t in enumerate(MOCK_TESTIMONIALS) if t['id'] == testimonial_id), None)
        if testimonial_index is None:
            return jsonify({
                'success': False,
                'error': 'Depoimento não encontrado'
            }), 404
        
        # Atualizar campos
        testimonial = MOCK_TESTIMONIALS[testimonial_index]
        for key, value in data.items():
            if key in testimonial:
                testimonial[key] = value
        
        return jsonify({
            'success': True,
            'data': testimonial
        })
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500

@testimonials_bp.route('/<testimonial_id>/approve', methods=['POST'])
def approve_testimonial(testimonial_id):
    """Aprovar depoimento"""
    try:
        # Encontrar depoimento
        testimonial_index = next((i for i, t in enumerate(MOCK_TESTIMONIALS) if t['id'] == testimonial_id), None)
        if testimonial_index is None:
            return jsonify({
                'success': False,
                'error': 'Depoimento não encontrado'
            }), 404
        
        # Aprovar depoimento
        MOCK_TESTIMONIALS[testimonial_index]['is_approved'] = True
        
        return jsonify({
            'success': True,
            'data': MOCK_TESTIMONIALS[testimonial_index],
            'message': 'Depoimento aprovado com sucesso!'
        })
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500

@testimonials_bp.route('/<testimonial_id>/feature', methods=['POST'])
def feature_testimonial(testimonial_id):
    """Destacar depoimento"""
    try:
        # Encontrar depoimento
        testimonial_index = next((i for i, t in enumerate(MOCK_TESTIMONIALS) if t['id'] == testimonial_id), None)
        if testimonial_index is None:
            return jsonify({
                'success': False,
                'error': 'Depoimento não encontrado'
            }), 404
        
        # Destacar depoimento
        MOCK_TESTIMONIALS[testimonial_index]['is_featured'] = True
        
        return jsonify({
            'success': True,
            'data': MOCK_TESTIMONIALS[testimonial_index],
            'message': 'Depoimento destacado com sucesso!'
        })
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500

@testimonials_bp.route('/<testimonial_id>', methods=['DELETE'])
def delete_testimonial(testimonial_id):
    """Excluir depoimento"""
    try:
        # Encontrar depoimento
        testimonial_index = next((i for i, t in enumerate(MOCK_TESTIMONIALS) if t['id'] == testimonial_id), None)
        if testimonial_index is None:
            return jsonify({
                'success': False,
                'error': 'Depoimento não encontrado'
            }), 404
        
        # Remover depoimento
        deleted_testimonial = MOCK_TESTIMONIALS.pop(testimonial_index)
        
        return jsonify({
            'success': True,
            'message': 'Depoimento excluído com sucesso!'
        })
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500

@testimonials_bp.route('/stats', methods=['GET'])
def get_testimonial_stats():
    """Obter estatísticas dos depoimentos"""
    try:
        total = len(MOCK_TESTIMONIALS)
        approved = len([t for t in MOCK_TESTIMONIALS if t['is_approved']])
        featured = len([t for t in MOCK_TESTIMONIALS if t['is_featured']])
        
        ratings = [t['rating'] for t in MOCK_TESTIMONIALS if t['is_approved']]
        avg_rating = sum(ratings) / len(ratings) if ratings else 0
        
        rating_distribution = {}
        for i in range(1, 6):
            rating_distribution[str(i)] = len([r for r in ratings if r == i])
        
        return jsonify({
            'success': True,
            'data': {
                'total': total,
                'approved': approved,
                'featured': featured,
                'pending_approval': total - approved,
                'average_rating': round(avg_rating, 1),
                'rating_distribution': rating_distribution
            }
        })
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500 