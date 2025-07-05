"""
Mestres do Café - Enterprise API
Sistema de e-commerce e ERP para torrefação artesanal
"""

import os
import sys
from dotenv import load_dotenv
from flask import Flask, jsonify
from flask_cors import CORS

# Carrega variáveis de ambiente
load_dotenv()

# Adiciona o diretório src ao path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

# Importações locais
from models.database import db

def create_app():
    """Factory function para criar a aplicação Flask"""
    app = Flask(__name__)
    
    # Configurações
    app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'dev-secret-key-change-in-production')
    app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL', 'sqlite:///mestres_cafe.db')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['JWT_SECRET_KEY'] = os.environ.get('JWT_SECRET_KEY', 'jwt-secret-change-in-production')
    
    # Inicializa extensões
    db.init_app(app)
    CORS(app, origins=["http://localhost:3000", "http://localhost:3001", "http://localhost:5173", "https://*.manus.space"])
    
    # Registrar blueprints
    from controllers.routes.products import products_bp
    from controllers.routes.testimonials import testimonials_bp
    from controllers.routes.courses import courses_bp
    
    app.register_blueprint(products_bp, url_prefix='/api/products')
    app.register_blueprint(testimonials_bp, url_prefix='/api/testimonials')
    app.register_blueprint(courses_bp, url_prefix='/api/courses')
    
    # Health check
    @app.route('/api/health')
    def health_check():
        return jsonify({
            'status': 'healthy',
            'service': 'Mestres do Café API',
            'version': '1.0.0',
            'environment': os.environ.get('FLASK_ENV', 'development')
        })
    
    # Rota de informações da API
    @app.route('/api/info')
    def api_info():
        return jsonify({
            'name': 'Mestres do Café Enterprise API',
            'version': '1.0.0',
            'description': 'Sistema de e-commerce e ERP para torrefação artesanal',
            'endpoints': {
                'health': '/api/health',
                'info': '/api/info',
                'products': '/api/products',
                'testimonials': '/api/testimonials',
                'courses': '/api/courses'
            }
        })
    
    return app

# Cria a aplicação
app = create_app()

if __name__ == '__main__':
    with app.app_context():
        # Cria as tabelas
        db.create_all()
    
    # Configurações do servidor
    port = int(os.environ.get('PORT', 5003))
    debug = os.environ.get('FLASK_ENV') == 'development'
    
    print(f"""
🚀 Mestres do Café Enterprise API
📍 Rodando em: http://localhost:{port}
🔧 API Health: http://localhost:{port}/api/health
📊 API Info: http://localhost:{port}/api/info
🐛 Debug: {debug}
    """)
    
    app.run(host='0.0.0.0', port=port, debug=debug)

