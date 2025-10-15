from cryptography.fernet import Fernet
from pymongo import MongoClient
import hashlib


#função de gerar hash-256
def gerar_hash(senha=""):
    hash_obj=hashlib.sha256(senha.encode())
    return hash_obj.hexdigest()
#função de verificar usuario existente
def verificar_user(senha=""):
    usuario_encontrado=collection.find_one({"senha":senha})
    if usuario_encontrado:
        hash_senha_inserida=gerar_hash(senha)
        if usuario_encontrado['hash_senha']==hash_senha_inserida:
            return True
    return False
#conexão com o MongoDB
client = MongoClient("mongodb+srv://root:123@cluster0.sqkox39.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
db = client["meubanco"]
collection = db["minhacolecao"]

senha=input("Insira sua senha:\n")
if verificar_user==True:
        print("Acesso permitido")
else:
        print("Não pode entrar")