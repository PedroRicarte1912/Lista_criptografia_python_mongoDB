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

mensagem=input("Insira sua mensagem:\n")
mensagem_hash=gerar_hash(mensagem)
resposta=input("Assinar mensagem:\n")
if resposta=="s":
  mensagem_cripto=fernet.encrypt(mensagem_hash.encode())
print(f"Mensagem criptografada:{mensagem_cripto}")
