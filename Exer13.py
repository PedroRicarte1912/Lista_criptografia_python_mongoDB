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

arquivo=input("Insira um arquivo:\n")
arquivo_fernt=fernet.encrypt(arquivo.encode())
hash_arq=gerar_hash(arquivo_fernt)
print("Dados criptografados!")
collection.insert_one({"arquivo":arquivo_fernt,"hash":hash_arq})
arquivo_achado=collection.find_one({"arquivo":arquivo_fernt})
if arquivo_achado["hash"]==hash_arq:
    print("Arquivos válidos e intregos!")
