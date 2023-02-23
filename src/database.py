from bson.objectid import ObjectId
from dotenv import load_dotenv
import motor.motor_asyncio
import bcrypt
import urllib
import os

load_dotenv()

PASSWORD_DB = urllib.parse.quote(os.environ["PASSWORD_DB"])
USER=os.environ["USER_DB"]
ADDRESS_DB=os.environ["ADDRESS_DB"]
MONGO_DETAILS = "mongodb://"+USER+":"+PASSWORD_DB+"@"+ADDRESS_DB


client = motor.motor_asyncio.AsyncIOMotorClient(MONGO_DETAILS)

database = client.users

users_collection = database.get_collection("users_collection")


# helpers

def users_helper(user) -> dict:
    return {"id": str(user["_id"]),
            "nome": user["nome"],
            "password": user["password"],
            "endereco": user["endereco"],
            "bairro": user["bairro"],
            "municipio": user["municipio"],
            "geolocalizacao": user["geolocalizacao"],
            "grupo": user["grupo"],
            "estabelecimento_comercial": user["estabelecimento_comercial"],
            "tipo_estabelecimento_comercial": user["tipo_estabelecimento_comercial"],
            "email": user["email"],
            "telefone": user["telefone"],
            "ativo": user["ativo"]}


#retorna todos os usuarios
async def retriev_users():
    users = []
    async for item in users_collection.find():
        users.append(users_helper(item))
    return users

#adiciona usuário
async def add_user(user_data: dict) -> dict:
    password_user= str(user_data['password'])
    password_user=password_user.encode('UTF-8')
   #encripta password
    hashedPassword = bcrypt.hashpw(password_user, bcrypt.gensalt())

    user_data['password']= hashedPassword

   #checa se existe já existe email cadastrado se sim retorna mensagem informado o usuário

    check_exists = await users_collection.find_one({"email": user_data['email']})    
    if check_exists:
        return False

    user = await users_collection.insert_one(user_data)
    new_user = await users_collection.find_one({"_id": user.inserted_id})

    return users_helper(new_user)

#retorna usuário especifico cadastrado
async def retriev_user(id: str) -> dict:
    user = await users_collection.find_one({"_id": ObjectId(id)})
    if user:
        return users_helper(user)

#atualiza cadastro
async def update_user(id: str, data: dict):
    if len(data) < 1:
        return False
    user = await users_collection.find_one({"_id": ObjectId(id)})
    if user:
        updated_user = await users_collection.update_one(
            {"_id": ObjectId(id)}, {"$set": data}
        )
        if updated_user:
            return True
        return False

#deleta
async def delete_user(id: str):
    user = await users_collection.find_one({"_id": ObjectId(id)})
    if user:
        await users_collection.delete_one({"_id": ObjectId(id)})
        return True
