from cryptography.fernet import Fernet
from pymongo import MongoClient
import hashlib


#função de gerar hash-256
def gerar_hash(senha=""):
    hash_obj=hashlib.sha256(senha.encode())
    return hash_obj.hexdigest()
#função para salvar usuário e senha
def salva_user(usuario="",senha=""):
    hash_senha=gerar_hash(senha)
    collection.insert_one({'usuario':usuario,'hash_senha':hash_senha})
#função de verificar usuario existente
def verificar_user(usuario="",senha=""):
    usuario_encontrado=collection.find_one({"usuario":usuario})
    if usuario_encontrado:
        hash_senha_inserida=gerar_hash(senha)
        if usuario_encontrado['hash_senha']==hash_senha_inserida:
            return True
    return False
#conexão com o MongoDB
client = MongoClient("mongodb+srv://root:123@cluster0.sqkox39.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
db = client["meubanco"]
collection = db["minhacolecao"]

resposta=input("Deseja entrar com um usuario(1) ou criar um(2)?")
if resposta == 1:
    print("Bem-vindo ao teste 1")
    usuario=input("Insira seu nome de usúario:\n")
    senha=input("Insira sua senha:\n")
    salva_user(usuario,senha)
if resposta==2:
    usuario=input("Insira seu nome de usúario:\n")
    senha=input("Insira sua senha:\n")
    if verificar_user==True:
        print("Acesso permitido")
    else:
        print("Não pode entrar")

