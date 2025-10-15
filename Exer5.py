from cryptography.fernet import Fernet
from pymongo import MongoClient
import hashlib

dados_cripto=[]

#função de gerar hash-256
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
#criptografia com fernet
valor=input("Insira o dado:\n")
valor_cripto=fernet.encrypt(valor.encode())
dados_cripto.append(valor_cripto)
#salvando hash
hash_dados=gerar_hash(valor_cripto)
collection.insert_one({"valor_hash":hash_dados})