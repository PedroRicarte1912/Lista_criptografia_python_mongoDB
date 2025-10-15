from cryptography.fernet import Fernet
from pymongo import MongoClient
import hashlib
import bcrypt


#conexão com o MongoDB
client = MongoClient("mongodb+srv://root:123@cluster0.sqkox39.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
db = client["meubanco"]
collection = db["minhacolecao"]

def registrar_usuario(nome_usuario, senha_texto_simples):
    """
    Gera o salt, hasheia a senha e armazena o hash no MongoDB.
    """
   
    senha_bytes = senha_texto_simples.encode('utf-8')
    
    
    hash_e_salt = bcrypt.hashpw(senha_bytes, bcrypt.gensalt())
    
    usuarios_collection = collection
    
    dados_usuario = {
        "username": nome_usuario,
        "senha_hash": hash_e_salt.decode('utf-8')
    }
    
    usuarios_collection.insert_one(dados_usuario)
    print(f"Usuário '{nome_usuario}' registrado com sucesso. Hash salvo: {dados_usuario['senha_hash']}")
    
def verificar_senha(nome_usuario, senha_candidata):
    """
    Busca o hash no MongoDB e compara a senha.
    """
    usuarios_collection = collection
    
  
    usuario = usuarios_collection.find_one({"username": nome_usuario})
    
    if not usuario:
        return False
    
    senha_hash_armazenada = usuario["senha_hash"]
    
   
    senha_candidata_bytes = senha_candidata.encode('utf-8')
    senha_hash_bytes = senha_hash_armazenada.encode('utf-8')
    
  
    if bcrypt.checkpw(senha_candidata_bytes, senha_hash_bytes):
        print(f"Autenticação bem-sucedida para o usuário '{nome_usuario}'.")
        return True
    else:
        print(f"Autenticação FALHOU para o usuário '{nome_usuario}'.")
        return False


USUARIO = "joao.silva"
SENHA = "MinhaSenhaSecreta123"


registrar_usuario(USUARIO, SENHA)


verificar_senha(USUARIO, SENHA) 
verificar_senha(USUARIO, "SenhaErrada") 
