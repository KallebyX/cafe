# ☕ Mestres do Café Enterprise

Sistema completo de e-commerce e ERP para torrefação artesanal de cafés especiais, desenvolvido com React + Flask.

## 🚀 Funcionalidades

### 🛒 **E-commerce Completo**
- Catálogo de produtos com filtros avançados
- Carrinho de compras e checkout
- Sistema de pagamentos integrado
- Gestão de pedidos e entregas

### 👥 **Sistema de Usuários**
- Autenticação completa (login/registro)
- Perfis de cliente e administrador
- Sistema de gamificação com pontos
- Gestão de permissões

### 📊 **Painel Administrativo Enterprise**
- **Dashboard**: Métricas em tempo real
- **Estoque**: Controle completo de produtos e inventário
- **CRM**: Gestão de clientes e relacionamentos
- **Financeiro**: Relatórios e controle de receitas/despesas
- **RH**: Gestão de funcionários e folha de pagamento
- **Compras**: Gestão de fornecedores e pedidos
- **Produção**: Controle de processo de torra
- **Analytics**: Business Intelligence e relatórios

### 🎓 **Plataforma Educacional**
- Cursos sobre café e barismo
- Blog com artigos especializados
- Fórum da comunidade
- Certificações

### 🌟 **Recursos Avançados**
- Sistema de depoimentos e avaliações
- Newsletter e marketing
- Integração com APIs de frete
- Sistema de notificações
- PWA (Progressive Web App)

## 🏗️ Arquitetura

### **Frontend** (React + Vite)
```
apps/web/
├── src/
│   ├── components/     # Componentes reutilizáveis
│   ├── pages/         # Páginas da aplicação
│   ├── contexts/      # Context API para estado global
│   ├── lib/          # APIs e utilitários
│   └── hooks/        # Custom hooks
└── public/           # Assets estáticos
```

### **Backend** (Flask + Python)
```
apps/api/
├── src/
│   ├── models/       # Modelos do banco de dados
│   ├── controllers/  # Rotas da API
│   ├── services/     # Lógica de negócio
│   └── utils/        # Utilitários
└── requirements.txt  # Dependências Python
```

## 🛠️ Tecnologias

### Frontend
- **React 18** - Framework principal
- **Vite** - Build tool e dev server
- **Tailwind CSS** - Estilização
- **Radix UI** - Componentes de interface
- **Recharts** - Gráficos e visualizações
- **React Router** - Navegação
- **Lucide React** - Ícones

### Backend
- **Flask** - Framework web Python
- **SQLAlchemy** - ORM para banco de dados
- **SQLite** - Banco de dados (desenvolvimento)
- **Flask-CORS** - Configuração de CORS

### Qualidade
- **ESLint** - Linting JavaScript
- **Prettier** - Formatação de código
- **Vitest** - Testes unitários

## 🚀 Como Executar

### Pré-requisitos
- Node.js 18+
- Python 3.11+
- npm ou yarn

### 1. Clone o repositório
```bash
git clone https://github.com/KallebyX/cafe.git
cd cafe
```

### 2. Instale as dependências
```bash
# Instalar todas as dependências
npm run install:all
```

### 3. Execute o projeto
```bash
# Executar frontend e backend simultaneamente
npm run dev
```

### 4. Acesse a aplicação
- **Frontend**: http://localhost:3000
- **Backend API**: http://localhost:5003
- **API Health**: http://localhost:5003/api/health

## 📋 Scripts Disponíveis

```bash
# Desenvolvimento
npm run dev              # Executar frontend + backend
npm run dev:web          # Apenas frontend
npm run dev:api          # Apenas backend

# Build
npm run build            # Build completo
npm run build:web        # Build do frontend
npm run build:api        # Build do backend

# Testes
npm run test             # Executar todos os testes
npm run test:web         # Testes do frontend
npm run test:api         # Testes do backend

# Qualidade
npm run lint             # Verificar código
npm run format           # Formatar código

# Utilitários
npm run clean            # Limpar cache e builds
npm run install:all      # Instalar todas as dependências
```

## 🗃️ Estrutura do Banco de Dados

### Principais Entidades
- **Users**: Usuários do sistema
- **Products**: Catálogo de produtos
- **Orders**: Pedidos e vendas
- **Customers**: Dados de clientes
- **Employees**: Funcionários
- **Suppliers**: Fornecedores
- **Courses**: Cursos educacionais
- **BlogPosts**: Artigos do blog
- **Testimonials**: Depoimentos

### Recursos Implementados
- Sistema de gamificação com pontos
- Gestão financeira completa
- Controle de estoque avançado
- CRM com histórico de interações
- Sistema de newsletter
- Análise de dados e métricas

## 🔧 Configuração

### Variáveis de Ambiente

Crie um arquivo `.env` na raiz do projeto:

```env
# Flask
SECRET_KEY=sua_chave_secreta_aqui
FLASK_ENV=development
DATABASE_URL=sqlite:///mestres_cafe.db

# JWT
JWT_SECRET_KEY=sua_chave_jwt_aqui

# APIs Externas (opcional)
MELHOR_ENVIO_TOKEN=token_melhor_envio
STRIPE_SECRET_KEY=sk_test_...
```

## 🚀 Deploy

### Opções de Deploy

1. **Vercel** (Frontend) + **Railway** (Backend)
2. **Heroku** (Fullstack)
3. **Docker** (Container)
4. **VPS** (Manual)

### Build para Produção

```bash
# Build otimizado
npm run build

# Arquivos gerados em:
# - apps/web/dist/       (Frontend)
# - apps/api/            (Backend pronto)
```

## 📊 Status do Projeto

### ✅ Funcionalidades Implementadas
- [x] Sistema de autenticação
- [x] Catálogo de produtos
- [x] Carrinho de compras
- [x] Painel administrativo
- [x] Dashboard com métricas
- [x] Gestão de estoque
- [x] CRM básico
- [x] Sistema de cursos
- [x] Blog integrado
- [x] API REST completa
- [x] Sistema de depoimentos
- [x] Componentes UI reutilizáveis

### 🔄 Em Desenvolvimento
- [ ] Integração de pagamentos
- [ ] Sistema de frete automático
- [ ] Notificações push
- [ ] App mobile (React Native)
- [ ] Analytics avançados

## 🤝 Contribuição

1. Fork o projeto
2. Crie uma branch (`git checkout -b feature/nova-funcionalidade`)
3. Commit suas mudanças (`git commit -m 'Adiciona nova funcionalidade'`)
4. Push para a branch (`git push origin feature/nova-funcionalidade`)
5. Abra um Pull Request

## 📄 Licença

Este projeto está sob a licença MIT. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.

## 👨‍💻 Autor

**KallebyX**
- GitHub: [@KallebyX](https://github.com/KallebyX)
- Projeto: [Mestres do Café](https://github.com/KallebyX/cafe)

---

**☕ Feito com ❤️ para os amantes de café especial**

