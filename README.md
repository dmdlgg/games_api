# 🎮 Games API

Uma API RESTful desenvolvida com Django REST Framework, projetada para fornecer informações sobre jogos de forma escalável, moderna e inteligente.
O projeto vai além do CRUD tradicional, incorporando integração com IA para geração automática de sinopses, endpoint de estatísticas avançadas, e autenticação JWT completa.
Além disso, segue boas práticas de código e padronização de estilo com o uso do linter Flake8 (seguindo a pep8), garantindo qualidade, legibilidade e manutenibilidade do código.

OBS: O projeto ainda está em desenvolvimento. Futuramente será feito o deploy via AWS e o desenvolvimento de um front-end para consumir a API.

---

## 🚀 Funcionalidades

- ✅ CRUD completo para gerenciamento de jogos  
- 🧠 **Integração com IA** para **geração automática de sinopses** de jogos  
- ⚙️ **Django Signals** para persistência e atualização automatizada das sinopses no banco de dados  
- 🔄 **Serializers dinâmicos**, permitindo respostas otimizadas conforme o contexto da requisição  
- 🧩 URLs preparadas para **versionamento da API** (`/api/v1/`, `/api/v2/`, ...)  
- 📊 **Endpoint de estatísticas** com informações agregadas sobre os jogos cadastrados  
- 🔐 **Autenticação e autorização via JWT** (JSON Web Tokens)

---

## 🏗️ Tecnologias utilizadas

- [Python 3.11+](https://www.python.org/)
- [Django 5+](https://www.djangoproject.com/)
- [Django REST Framework](https://www.django-rest-framework.org/)
- [SimpleJWT](https://django-rest-framework-simplejwt.readthedocs.io/en/latest/)
- [OpenAI / IA API](https://platform.openai.com/) *(para geração das sinopses)*
- Banco de dados (SQLite)

---

## ⚙️ Instalação e uso

### 1️⃣ Clone o repositório
```bash
git clone https://github.com/dmdlgg/games_api.git
cd games_api
```

### 2️⃣ Crie um ambiente virtual 
``` bash
python -m venv venv
source venv/bin/activate  # Linux / Mac
venv\Scripts\activate     # Windows
``` 

### 3️⃣ Instale as depedências
```bash
pip install -r requirements.txt 
pip install -r requirements_dev.txt 
```

4️⃣ Configure variáveis de ambiente
Crie um arquivo .env na raiz do projeto e adicione:
``` bash
OPENAI_API_KEY = sua_chave_de_api
```
### 5️⃣ Execute as migrações
```bash
python manage.py migrate
```

### 6️⃣ Inicie o servidor
```bash
python manage.py runserver
```
---

## 🔑 Autenticação JWT
- Para obter o token, basta fazer um POST com o usuário e senha no endpoint /api/v1/autenticacao/token/
  ```bash
  {
  "username": "seu_usuario",
  "password": "sua_senha"
  }
  ```
  Inclua o o token JWT nos headers para acessar os endpoints protegidos
---

## 🧠 IA e Django Signals
- A cada novo jogo cadastrado, o sistema envia o nome e o diretor do jogo para a API da OpenAI, que gera automaticamente uma sinopse personalizada.
Essa sinopse é então salva no banco de dados através de um Django Signal, garantindo persistência automática e desacoplada da lógica principal.
### Exemplo do fluxo:
  -> Usuário cadastra um novo jogo (POST /api/v1/jogos/)

  -> O Django Signal detecta a criação do registro

  -> Se o campo de sinopse estiver vazio, o a API da OpenAI é chamada passando os dados do jogo

  -> A sinopse é gerada e salva automaticamente no banco
---

## Endpoints Principais:
|    Método   | Endpoint                   | Descrição                           |
| :---------: | :--------------------- | :-------------------------------------- |
|    `GET`    | `/api/v1/jogos/`       | Lista todos os jogos                    |
|    `POST`   | `/api/v1/jogos/`       | Cria um novo jogo                       |
|    `GET`    | `/api/v1/jogos/<id>/`  | Detalhes de um jogo                     |
| `PUT/PATCH` | `/api/v1/jogos/<id>/`  | Atualiza um jogo                        |
|   `DELETE`  | `/api/v1/jogos/<id>/`  | Remove um jogo                          |
|    `GET`    | `/api/v1/stats/`       | Retorna estatísticas sobre os jogos     |

---
## 📬 Contato

Fique à vontade para entrar em contato caso tenha dúvidas, sugestões ou queira contribuir:
  
- 📨 **Email:** dumedolago@gmail.com 
- 💻 **Linkedin:** [Eduardo Medolago](https://www.linkedin.com/in/eduardo-medolago-364288259/)

