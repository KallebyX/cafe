"""
Rotas de produtos para a API Mestres do Café
"""

from flask import Blueprint, request, jsonify

# Criar blueprint
products_bp = Blueprint('products', __name__)

# Dados mock para desenvolvimento
MOCK_PRODUCTS = [
    {
        'id': '1',
        'name': 'Café Especial do Brasil',
        'description': 'Café 100% arábica da região de Minas Gerais',
        'price': 25.90,
        'image_url': 'https://images.unsplash.com/photo-1447933601403-0c6688de566e?w=400',
        'category': 'Especiais',
        'origin': 'Minas Gerais, Brasil',
        'process': 'Natural',
        'variety': 'Bourbon',
        'sca_score': 85,
        'roast_level': 'Médio',
        'stock_quantity': 50,
        'is_active': True
    },
    {
        'id': '2',
        'name': 'Café Gourmet Colombiano',
        'description': 'Café premium da região de Huila, Colômbia',
        'price': 32.50,
        'image_url': 'https://images.unsplash.com/photo-1509042239860-f550ce710b93?w=400',
        'category': 'Gourmet',
        'origin': 'Huila, Colômbia',
        'process': 'Lavado',
        'variety': 'Caturra',
        'sca_score': 88,
        'roast_level': 'Médio-Claro',
        'stock_quantity': 30,
        'is_active': True
    },
    {
        'id': '3',
        'name': 'Café Etíope Natural',
        'description': 'Café da berço do café, com notas florais únicas',
        'price': 45.00,
        'image_url': 'https://images.unsplash.com/photo-1559056199-641a0ac8b55e?w=400',
        'category': 'Especiais',
        'origin': 'Yirgacheffe, Etiópia',
        'process': 'Natural',
        'variety': 'Heirloom',
        'sca_score': 92,
        'roast_level': 'Claro',
        'stock_quantity': 20,
        'is_active': True
    },
    {
        'id': '4',
        'name': 'Café Premium Guatemala',
        'description': 'Café de altitude da região de Antigua',
        'price': 38.90,
        'image_url': 'https://images.unsplash.com/photo-1497935586351-b67a49e012bf?w=400',
        'category': 'Gourmet',
        'origin': 'Antigua, Guatemala',
        'process': 'Lavado',
        'variety': 'Típica',
        'sca_score': 86,
        'roast_level': 'Médio',
        'stock_quantity': 25,
        'is_active': True
    }
]

MOCK_CATEGORIES = [
    {'id': '1', 'name': 'Especiais', 'description': 'Cafés especiais com alta pontuação SCA'},
    {'id': '2', 'name': 'Gourmet', 'description': 'Cafés premium de origem única'},
    {'id': '3', 'name': 'Blend', 'description': 'Misturas equilibradas de diferentes origens'},
    {'id': '4', 'name': 'Orgânicos', 'description': 'Cafés cultivados sem agrotóxicos'}
]

MOCK_ROAST_LEVELS = [
    {'id': '1', 'name': 'Claro', 'description': 'Torra clara, preserva acidez e aromas florais'},
    {'id': '2', 'name': 'Médio-Claro', 'description': 'Torra média-clara, equilibra acidez e corpo'},
    {'id': '3', 'name': 'Médio', 'description': 'Torra média, corpo equilibrado'},
    {'id': '4', 'name': 'Médio-Escuro', 'description': 'Torra média-escura, corpo mais acentuado'},
    {'id': '5', 'name': 'Escuro', 'description': 'Torra escura, corpo intenso e baixa acidez'}
]

@products_bp.route('', methods=['GET'])
def get_all_products():
    """Listar todos os produtos"""
    try:
        return jsonify({
            'success': True,
            'data': MOCK_PRODUCTS,
            'total': len(MOCK_PRODUCTS)
        })
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500

@products_bp.route('/filtered', methods=['POST'])
def get_filtered_products():
    """Listar produtos com filtros"""
    try:
        data = request.get_json() or {}
        
        # Para desenvolvimento, retornar produtos mockados
        filtered_products = MOCK_PRODUCTS.copy()
        
        # Aplicar filtros básicos
        if 'category' in data and data['category']:
            filtered_products = [p for p in filtered_products if p['category'] == data['category']]
        
        if 'roast_level' in data and data['roast_level']:
            filtered_products = [p for p in filtered_products if p['roast_level'] == data['roast_level']]
        
        if 'min_price' in data and data['min_price']:
            filtered_products = [p for p in filtered_products if p['price'] >= data['min_price']]
        
        if 'max_price' in data and data['max_price']:
            filtered_products = [p for p in filtered_products if p['price'] <= data['max_price']]
        
        return jsonify({
            'success': True,
            'data': filtered_products,
            'total': len(filtered_products)
        })
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500

@products_bp.route('/<product_id>', methods=['GET'])
def get_product(product_id):
    """Obter produto específico"""
    try:
        product = next((p for p in MOCK_PRODUCTS if p['id'] == product_id), None)
        if not product:
            return jsonify({
                'success': False,
                'error': 'Produto não encontrado'
            }), 404
        
        return jsonify({
            'success': True,
            'data': product
        })
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500

@products_bp.route('/categories', methods=['GET'])
def get_categories():
    """Listar categorias de produtos"""
    try:
        return jsonify({
            'success': True,
            'data': MOCK_CATEGORIES
        })
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500

@products_bp.route('/featured', methods=['GET'])
def get_featured_products():
    """Obter produtos em destaque"""
    try:
        # Produtos com maior pontuação SCA
        featured = [p for p in MOCK_PRODUCTS if p['sca_score'] >= 86]
        featured.sort(key=lambda x: x['sca_score'], reverse=True)
        
        return jsonify({
            'success': True,
            'data': featured[:3]  # Top 3 produtos
        })
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500

@products_bp.route('', methods=['POST'])
def create_product():
    """Criar novo produto"""
    try:
        data = request.get_json()
        
        # Validação básica
        if not data or 'name' not in data or 'price' not in data:
            return jsonify({
                'success': False,
                'error': 'Nome e preço são obrigatórios'
            }), 400
        
        # Simular criação do produto
        new_product = {
            'id': str(len(MOCK_PRODUCTS) + 1),
            'name': data['name'],
            'description': data.get('description', ''),
            'price': float(data['price']),
            'image_url': data.get('image_url', ''),
            'category': data.get('category', ''),
            'origin': data.get('origin', ''),
            'process': data.get('process', ''),
            'variety': data.get('variety', ''),
            'sca_score': data.get('sca_score', 0),
            'roast_level': data.get('roast_level', ''),
            'stock_quantity': data.get('stock_quantity', 0),
            'is_active': True
        }
        
        MOCK_PRODUCTS.append(new_product)
        
        return jsonify({
            'success': True,
            'data': new_product
        }), 201
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500

@products_bp.route('/<product_id>', methods=['PUT'])
def update_product(product_id):
    """Atualizar produto"""
    try:
        data = request.get_json()
        
        # Encontrar produto
        product_index = next((i for i, p in enumerate(MOCK_PRODUCTS) if p['id'] == product_id), None)
        if product_index is None:
            return jsonify({
                'success': False,
                'error': 'Produto não encontrado'
            }), 404
        
        # Atualizar campos
        product = MOCK_PRODUCTS[product_index]
        for key, value in data.items():
            if key in product:
                product[key] = value
        
        return jsonify({
            'success': True,
            'data': product
        })
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500

@products_bp.route('/roast-levels', methods=['GET'])
def get_roast_levels():
    """Listar níveis de torra"""
    try:
        return jsonify({
            'success': True,
            'data': MOCK_ROAST_LEVELS
        })
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500

@products_bp.route('/validate', methods=['POST'])
def validate_product():
    """Validar dados do produto"""
    try:
        data = request.get_json()
        
        errors = []
        
        # Validações básicas
        if not data.get('name'):
            errors.append('Nome é obrigatório')
        
        if not data.get('price'):
            errors.append('Preço é obrigatório')
        else:
            try:
                price = float(data['price'])
                if price <= 0:
                    errors.append('Preço deve ser maior que zero')
            except ValueError:
                errors.append('Preço deve ser um número válido')
        
        if data.get('sca_score'):
            try:
                score = int(data['sca_score'])
                if score < 0 or score > 100:
                    errors.append('Pontuação SCA deve ser entre 0 e 100')
            except ValueError:
                errors.append('Pontuação SCA deve ser um número inteiro')
        
        return jsonify({
            'success': len(errors) == 0,
            'errors': errors
        })
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500

