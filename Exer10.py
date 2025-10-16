from cryptography.fernet import Fernet
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
#Gerando chave Fernet
key = Fernet.generate_key()
fernet = Fernet(key)

voto=input("Insira seu voto:\n")
voto_cripto=fernet.encrypt(voto.encode())
print(f"Seu voto com criptografia fernet:{voto_cripto}\n")
voto_hash=gerar_hash(voto_cripto)
collection.insert_one({"voto":voto_cripto,"hash voto":voto_hash})
