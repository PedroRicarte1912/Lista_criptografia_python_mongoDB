from cryptography.fernet import Fernet
from pymongo import MongoClient
import hashlib

#função para gerar o hash com sha-256
def gerar_hash(senha=""):
    hash_obj=hashlib.sha512(senha.encode())
    return hash_obj.hexdigest()
#conexão com o MongoDB
client = MongoClient("mongodb+srv://root:123@cluster0.sqkox39.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
db = client["meubanco"]
collection = db["minhacolecao"]
#Gerando chave Fernet
key = Fernet.generate_key()
fernet = Fernet(key)
#solicitação ao usuário
certificado=[]
hash_cert=[]
certificado_cripto=[]
resposta=input("deseja inserir certificados:\n")
while resposta=="s":
    certificado=input("Insira seu certificado aqui:\n")
    certificado_cripto=fernet.encrypt(certificado.encode())
    hash_cert=gerar_hash(certificado_cripto)
    for i in range (0,certificado.lenght()):
        collection._insert_one({"certificado":certificado_cripto[i],"hash":hash_cert[i]})
