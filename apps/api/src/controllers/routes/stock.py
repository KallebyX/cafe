from flask import Blueprint

stock_bp = Blueprint('stock', __name__)

# TODO: Implementar rotas de stock após corrigir problemas de import
@stock_bp.route('/api/stock/health', methods=['GET'])
def stock_health():
    """Health check para o módulo de stock"""
    return {'status': 'Stock module disabled temporarily'}, 200

# Todas as outras rotas foram temporariamente comentadas para evitar erros de import
# que impedem a inicialização da API 