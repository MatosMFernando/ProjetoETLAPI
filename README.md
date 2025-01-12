# 🪙 Projeto ETL de Dados de Criptomoedas

## 📋 Descrição
Este projeto consiste em um pipeline ETL (Extract, Transform, Load) que coleta dados de criptomoedas em tempo real através de APIs públicas, processa essas informações e armazena em um banco de dados para análises posteriores.

## 🚀 Funcionalidades
- Extração de dados em tempo real da API de criptomoedas
- Processamento e limpeza dos dados obtidos
- Armazenamento em banco de dados SQL/NoSQL
- Geração de relatórios automáticos
- Monitoramento de preços e volumes de trading

## 🛠️ Tecnologias Utilizadas
- Python 3.9+
- Pandas para manipulação de dados
- Requests para chamadas API
- SQLAlchemy para ORM
- PostgreSQL como banco de dados
- Docker para containerização

## 📦 Estrutura do Projeto
```
crypto-etl/
├── src/
│   ├── extractors/
│   ├── transformers/
│   ├── loaders/
│   └── utils/
├── config/
├── tests/
├── docs/
└── docker/
```

## 🔧 Configuração e Instalação

1. Clone o repositório:
```bash
git clone https://github.com/seu-usuario/crypto-etl.git
cd crypto-etl
```

2. Crie um ambiente virtual:
```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows
```

3. Instale as dependências:
```bash
pip install -r requirements.txt
```

4. Configure as variáveis de ambiente:
```bash
cp .env.example .env
# Edite o arquivo .env com suas configurações
```

## 🚀 Como Executar

```bash
python src/main.py
```

## 📊 Exemplo de Uso
```python
from crypto_etl.extractors import CryptoAPIExtractor
from crypto_etl.transformers import DataTransformer
from crypto_etl.loaders import DatabaseLoader

# Iniciar o pipeline
extractor = CryptoAPIExtractor()
transformer = DataTransformer()
loader = DatabaseLoader()

# Executar ETL
data = extractor.extract()
transformed_data = transformer.transform(data)
loader.load(transformed_data)
```

## 📝 Configuração da API
O projeto utiliza a API [nome_da_api] para coletar dados. É necessário:
1. Criar uma conta em [link_da_api]
2. Gerar uma API key
3. Adicionar a key no arquivo `.env`

## 🤝 Contribuindo
1. Faça um Fork do projeto
2. Crie uma branch para sua feature (`git checkout -b feature/AmazingFeature`)
3. Commit suas mudanças (`git commit -m 'Add some AmazingFeature'`)
4. Push para a branch (`git push origin feature/AmazingFeature`)
5. Abra um Pull Request


## 📄 Licença
Este projeto está sob a licença MIT. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.
