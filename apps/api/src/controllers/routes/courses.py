"""
Rotas de cursos para a API Mestres do Café
"""

from flask import Blueprint, jsonify, request
from datetime import datetime, timedelta

# Criar blueprint
courses_bp = Blueprint('courses', __name__)

# Dados mock para desenvolvimento
MOCK_COURSES = [
    {
        'id': '1',
        'title': 'Curso de Barista Profissional',
        'description': 'Aprenda todas as técnicas para se tornar um barista profissional, desde a seleção dos grãos até o preparo perfeito.',
        'price': 299.90,
        'instructor': 'Carlos Mendes',
        'image_url': 'https://images.unsplash.com/photo-1501339847302-ac426a4a7cbb?w=500',
        'status': 'active',
        'start_date': '2024-02-15T09:00:00Z',
        'end_date': '2024-02-17T17:00:00Z',
        'duration_hours': 24,
        'max_students': 20,
        'enrolled_students': 15,
        'category': 'Barista',
        'level': 'Iniciante',
        'includes': ['Certificado', 'Kit de materiais', 'Coffee breaks'],
        'topics': [
            'História do café',
            'Tipos de grãos e torras',
            'Técnicas de extração',
            'Latte art básico',
            'Atendimento ao cliente'
        ],
        'requirements': 'Nenhum conhecimento prévio necessário',
        'created_at': '2024-01-01T10:00:00Z'
    },
    {
        'id': '2',
        'title': 'Degustação e Análise Sensorial',
        'description': 'Desenvolva seu paladar e aprenda a identificar as características únicas de cada café especial.',
        'price': 199.90,
        'instructor': 'Ana Costa',
        'image_url': 'https://images.unsplash.com/photo-1442512595331-e89e73853f31?w=500',
        'status': 'active',
        'start_date': '2024-03-01T14:00:00Z',
        'end_date': '2024-03-01T18:00:00Z',
        'duration_hours': 4,
        'max_students': 15,
        'enrolled_students': 8,
        'category': 'Degustação',
        'level': 'Intermediário',
        'includes': ['Certificado', 'Amostras de café', 'Guia de degustação'],
        'topics': [
            'Anatomia do paladar',
            'Roda de sabores do café',
            'Técnicas de cupping',
            'Identificação de defeitos',
            'Pontuação SCA'
        ],
        'requirements': 'Conhecimento básico sobre café',
        'created_at': '2024-01-05T10:00:00Z'
    },
    {
        'id': '3',
        'title': 'Métodos de Extração Alternativos',
        'description': 'Explore diferentes métodos de preparo como V60, Chemex, AeroPress e French Press.',
        'price': 249.90,
        'instructor': 'João Silva',
        'image_url': 'https://images.unsplash.com/photo-1495774856032-8b90bbb32b32?w=500',
        'status': 'active',
        'start_date': '2024-02-20T09:00:00Z',
        'end_date': '2024-02-21T17:00:00Z',
        'duration_hours': 16,
        'max_students': 12,
        'enrolled_students': 10,
        'category': 'Métodos',
        'level': 'Intermediário',
        'includes': ['Certificado', 'Kit V60', 'Receitas exclusivas'],
        'topics': [
            'Teoria da extração',
            'V60 e Hario',
            'Chemex e filtros',
            'AeroPress técnicas',
            'French Press e Clever'
        ],
        'requirements': 'Curso de Barista ou experiência equivalente',
        'created_at': '2024-01-10T10:00:00Z'
    },
    {
        'id': '4',
        'title': 'Torra Artesanal para Iniciantes',
        'description': 'Aprenda os fundamentos da torra de café e desenvolva seus próprios perfis de torra.',
        'price': 399.90,
        'instructor': 'Roberto Santos',
        'image_url': 'https://images.unsplash.com/photo-1587734195503-904fca47e0e9?w=500',
        'status': 'planned',
        'start_date': '2024-04-01T09:00:00Z',
        'end_date': '2024-04-03T17:00:00Z',
        'duration_hours': 24,
        'max_students': 10,
        'enrolled_students': 0,
        'category': 'Torra',
        'level': 'Avançado',
        'includes': ['Certificado', 'Amostras de café verde', 'Manual de torra'],
        'topics': [
            'Física da torra',
            'Curvas de desenvolvimento',
            'Perfis de sabor',
            'Controle de qualidade',
            'Equipamentos de torra'
        ],
        'requirements': 'Experiência prévia com café recomendada',
        'created_at': '2024-01-15T10:00:00Z'
    }
]

@courses_bp.route('', methods=['GET'])
def get_all_courses():
    """Listar todos os cursos"""
    try:
        return jsonify({
            'success': True,
            'data': MOCK_COURSES,
            'total': len(MOCK_COURSES)
        })
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500

@courses_bp.route('/active', methods=['GET'])
def get_active_courses():
    """Listar cursos ativos"""
    try:
        active_courses = [c for c in MOCK_COURSES if c['status'] == 'active']
        
        return jsonify({
            'success': True,
            'data': active_courses,
            'total': len(active_courses)
        })
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500

@courses_bp.route('/upcoming', methods=['GET'])
def get_upcoming_courses():
    """Listar cursos que vão começar em breve"""
    try:
        now = datetime.now()
        upcoming = []
        
        for course in MOCK_COURSES:
            if course['status'] == 'active':
                start_date = datetime.fromisoformat(course['start_date'].replace('Z', '+00:00'))
                if start_date > now:
                    upcoming.append(course)
        
        # Ordenar por data de início
        upcoming.sort(key=lambda x: x['start_date'])
        
        return jsonify({
            'success': True,
            'data': upcoming,
            'total': len(upcoming)
        })
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500

@courses_bp.route('/<course_id>', methods=['GET'])
def get_course(course_id):
    """Obter curso específico"""
    try:
        course = next((c for c in MOCK_COURSES if c['id'] == course_id), None)
        if not course:
            return jsonify({
                'success': False,
                'error': 'Curso não encontrado'
            }), 404
        
        return jsonify({
            'success': True,
            'data': course
        })
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500

@courses_bp.route('/categories', methods=['GET'])
def get_course_categories():
    """Listar categorias de cursos"""
    try:
        categories = list(set([c['category'] for c in MOCK_COURSES]))
        category_data = []
        
        for cat in categories:
            courses_count = len([c for c in MOCK_COURSES if c['category'] == cat])
            category_data.append({
                'name': cat,
                'count': courses_count
            })
        
        return jsonify({
            'success': True,
            'data': category_data
        })
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500

@courses_bp.route('/levels', methods=['GET'])
def get_course_levels():
    """Listar níveis de dificuldade"""
    try:
        levels = ['Iniciante', 'Intermediário', 'Avançado']
        level_data = []
        
        for level in levels:
            courses_count = len([c for c in MOCK_COURSES if c['level'] == level])
            level_data.append({
                'name': level,
                'count': courses_count
            })
        
        return jsonify({
            'success': True,
            'data': level_data
        })
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500

@courses_bp.route('', methods=['POST'])
def create_course():
    """Criar novo curso"""
    try:
        data = request.get_json()
        
        # Validação básica
        if not data or 'title' not in data or 'price' not in data:
            return jsonify({
                'success': False,
                'error': 'Título e preço são obrigatórios'
            }), 400
        
        # Simular criação do curso
        new_course = {
            'id': str(len(MOCK_COURSES) + 1),
            'title': data['title'],
            'description': data.get('description', ''),
            'price': float(data['price']),
            'instructor': data.get('instructor', ''),
            'image_url': data.get('image_url', ''),
            'status': data.get('status', 'planned'),
            'start_date': data.get('start_date', ''),
            'end_date': data.get('end_date', ''),
            'duration_hours': data.get('duration_hours', 0),
            'max_students': data.get('max_students', 20),
            'enrolled_students': 0,
            'category': data.get('category', ''),
            'level': data.get('level', 'Iniciante'),
            'includes': data.get('includes', []),
            'topics': data.get('topics', []),
            'requirements': data.get('requirements', ''),
            'created_at': datetime.now().isoformat() + 'Z'
        }
        
        MOCK_COURSES.append(new_course)
        
        return jsonify({
            'success': True,
            'data': new_course
        }), 201
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500

@courses_bp.route('/<course_id>', methods=['PUT'])
def update_course(course_id):
    """Atualizar curso"""
    try:
        data = request.get_json()
        
        # Encontrar curso
        course_index = next((i for i, c in enumerate(MOCK_COURSES) if c['id'] == course_id), None)
        if course_index is None:
            return jsonify({
                'success': False,
                'error': 'Curso não encontrado'
            }), 404
        
        # Atualizar campos
        course = MOCK_COURSES[course_index]
        for key, value in data.items():
            if key in course:
                course[key] = value
        
        return jsonify({
            'success': True,
            'data': course
        })
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500

@courses_bp.route('/<course_id>/enroll', methods=['POST'])
def enroll_in_course(course_id):
    """Inscrever-se em um curso"""
    try:
        data = request.get_json()
        
        # Encontrar curso
        course_index = next((i for i, c in enumerate(MOCK_COURSES) if c['id'] == course_id), None)
        if course_index is None:
            return jsonify({
                'success': False,
                'error': 'Curso não encontrado'
            }), 404
        
        course = MOCK_COURSES[course_index]
        
        # Verificar se há vagas
        if course['enrolled_students'] >= course['max_students']:
            return jsonify({
                'success': False,
                'error': 'Curso lotado'
            }), 400
        
        # Verificar se o curso está ativo
        if course['status'] != 'active':
            return jsonify({
                'success': False,
                'error': 'Curso não está disponível para inscrição'
            }), 400
        
        # Simular inscrição
        MOCK_COURSES[course_index]['enrolled_students'] += 1
        
        return jsonify({
            'success': True,
            'message': 'Inscrição realizada com sucesso!',
            'data': {
                'course_id': course_id,
                'course_title': course['title'],
                'enrolled_students': course['enrolled_students'],
                'available_spots': course['max_students'] - course['enrolled_students']
            }
        })
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500

@courses_bp.route('/stats', methods=['GET'])
def get_course_stats():
    """Obter estatísticas dos cursos"""
    try:
        total = len(MOCK_COURSES)
        active = len([c for c in MOCK_COURSES if c['status'] == 'active'])
        planned = len([c for c in MOCK_COURSES if c['status'] == 'planned'])
        
        total_enrolled = sum([c['enrolled_students'] for c in MOCK_COURSES])
        total_capacity = sum([c['max_students'] for c in MOCK_COURSES])
        
        avg_price = sum([c['price'] for c in MOCK_COURSES]) / total if total > 0 else 0
        
        return jsonify({
            'success': True,
            'data': {
                'total_courses': total,
                'active_courses': active,
                'planned_courses': planned,
                'total_enrolled': total_enrolled,
                'total_capacity': total_capacity,
                'occupancy_rate': round((total_enrolled / total_capacity) * 100, 1) if total_capacity > 0 else 0,
                'average_price': round(avg_price, 2)
            }
        })
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500 