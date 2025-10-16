from pymongo import MongoClient
import hashlib

#função para gerar o hash com sha-256
def gerar_hash(senha=""):
    hash_obj=hashlib.sha256(senha.encode())
    return hash_obj.hexdigest()
#conexão com o MongoDB

client = MongoClient("mongodb+srv://root:123@cluster0.sqkox39.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
db = client["meubanco"]
collection = db["minhacolecao"]

dado_user=""
dado_user="facialusuario1"
dado_hash=gerar_hash(dado_user)
collection.insert_one({"dado":dado_user,"hash":dado_hash})
print(f"Dado normal:{dado_user}\n dado com hash:{dado_hash}\n")