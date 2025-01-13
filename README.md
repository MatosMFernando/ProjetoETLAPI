## Exemplo de Integração com a API OpenAI

Este é um exemplo simples de como integrar com a API da OpenAI usando Python para fazer perguntas ao modelo GPT-3.5-turbo.

## Pré-requisitos

- Python 3.6 ou superior
- Uma chave de API da OpenAI

## Instalação

1. Clone este repositório ou baixe os arquivos

2. Crie um ambiente virtual (recomendado):
```bash
python -m venv venv
```

3. Ative o ambiente virtual:

**Windows:**
```bash
venv\Scripts\activate
```

**Linux/Mac:**
```bash
source venv/bin/activate
```

4. Instale as dependências:
```bash
pip install -r requirements.txt
```

5. Configure as variáveis de ambiente:
   - Crie um arquivo `.env` na raiz do projeto
   - Adicione sua chave da API da OpenAI:
```
OPEN_AI_KEY=sua_chave_api_aqui
```

## Como usar

1. Execute o script:
```bash
python exemplos/exemplo04.py
```

O script fará uma pergunta simples à API da OpenAI ("Qual é a capital da França?") e mostrará o código de status da resposta.

## Estrutura do requirements.txt

Crie um arquivo `requirements.txt` com as seguintes dependências:
```text
requests==2.31.0
python-dotenv==1.0.0
```

## Como funciona

O script utiliza:
- `requests`: para fazer chamadas HTTP à API da OpenAI
- `python-dotenv`: para gerenciar variáveis de ambiente de forma segura
- `json`: para manipular dados JSON na requisição
- `os`: para acessar variáveis de ambiente

A API é chamada com os headers apropriados e um payload contendo o modelo a ser usado e a mensagem do usuário.

## Observações

- Mantenha sua chave de API segura e nunca a compartilhe ou cometa no controle de versão
- O arquivo `.env` deve ser adicionado ao `.gitignore`
- Verifique sempre a documentação oficial da OpenAI para atualizações na API

## Suporte

Para dúvidas ou problemas, abra uma issue no repositório.