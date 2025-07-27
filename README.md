# 🧬 Django API REST

API RESTful construída com Django e Django REST Framework, com foco em boas práticas, modularidade e escalabilidade.

---

## 🚀 Tecnologias Utilizadas

- Python 3.11+
- Django 5.x
- Django REST Framework
- SQLite (default)
- Python Decouple (para variáveis de ambiente)

---

## 📦 Instalação e Execução

1️⃣ **Clone o repositório**
```bash
git clone https://github.com/guzenskicg/django-api-rest.git
cd django-api-rest

2️⃣ Crie e ative o ambiente virtual
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows

3️⃣ Instale as dependências
pip install -r requirements.txt

4️⃣ Configure variáveis de ambiente
Crie um arquivo .env na raiz com:
DEBUG=True
SECRET_KEY=sua_chave_secreta
ALLOWED_HOSTS=127.0.0.1,localhost

5️⃣ Execute as migrações
python manage.py migrate

6️⃣ Inicie o servidor
python manage.py runserver

📡 Endpoints da API
| Método | Rota | Descrição | 
| GET | /api/ | Endpoint inicial | 
| POST | /api/... | Criar recurso | 
| PUT | /api/... | Atualizar recurso | 
| DELETE | /api/... | Remover recurso | 

⚠️ Os endpoints ainda estão em desenvolvimento. Recomenda-se o uso de ferramentas como Postman para testes.

🧪 Testes
Em breve serão adicionados testes com pytest e APIClient.

📚 Contribuindo
- Fork o projeto
- Crie sua branch: git checkout -b feature/nova-feature
- Commit suas alterações: git commit -m 'feat: nova feature'
- Push para sua branch: git push origin feature/nova-feature
- Abra um Pull Request

📖 Licença
Este projeto está sob a licença MIT.

✉️ Contato
Desenvolvido por Charles Guzenski 💻
