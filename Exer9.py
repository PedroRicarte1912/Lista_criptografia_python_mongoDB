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

dado=input("Insira um dado para teste de hash:\n")
hash_dado=gerar_hash(dado)
collection.insert_one({"hash do dado":hash_dado})

dadox=collection.find_one({"hash do dado":dado})
if dadox==True:
    if dadox["hash do dado"]==hash_dado:
        print("Integridade do banco ok!")