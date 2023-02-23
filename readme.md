<h3>CRUD FASTAPI E MONGODB</h3>
<h4>python version 3.10.9</h4>

<br/>

<h4>Entre no diretorio do projeto e execute os comandos :</h4>

<br/>

<h4>pyenv install 3.10.9</h4>

<h4>pyenv local 3.10.9</h4> 

<h4>python -m venv venv/<h4> 

<h4>source venv/bin/activate</h4>

<br/>

<p>Instale as dependências:</p>

<h4>pip install -r requirements.txt</h4>

<br/>

<p>Crie arquivo .env na pasta src/ e insira as seguintes variavéis:<p>

<h5>PASSWORD_DB="pass"</h5>

<h5>USER_DB="user"</h5>

<h5>ADDRESS_DB="localhost:27017"</h5>

<br/>
<p>Rodando FastAPI:</p>

<h4> uvicorn main:app --reload </h4>
<br/>

http://localhost:8000/docs

<br/>

<p>Instalação mongodb via docker visite:</p>

https://www.mongodb.com/compatibility/docker









