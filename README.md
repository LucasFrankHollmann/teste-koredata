# teste-koredata

Passos para rodar o projeto:

### Backend
- Clone o repositório
```git clone https://github.com/LucasFrankHollmann/teste-koredata.git```
- Acesse o diretório do repositório 
```cd teste-koredata```
- Instale o Python caso não tenha
- Crie um ambiente virtual para executar o projeto backend
```python -m venv venv```
- Ative o ambiente virtual
```venv\Scripts\activate```
- Acesse o diretório do projeto backend 
```cd testekoredata```
- Instale as dependências
```pip install -r requirements.txt```
- Configure as informações do banco de dados no arquivo ```testekoredata\testekoredata\settings.py```
  <img width="400" height="239" alt="image" src="https://github.com/user-attachments/assets/a4545c56-77df-4122-a7dc-f8aabdd45412" />
- Execute as migrations ```python manage.py migrate```
- Execute o servidor backend ```python manage.py runserver 8000```

### Frontend
- Acesse o diretório do frontend a partir da raiz do repositório ```cd frontend```
- Instale as dependências do projeto ```npm install```
- Rode o projeto ```npm run dev```
