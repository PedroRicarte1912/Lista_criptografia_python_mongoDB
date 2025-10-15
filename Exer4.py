from cryptography.fernet import Fernet
from pymongo import MongoClient

#conexão com o MongoDB
client = MongoClient("mongodb+srv://root:123@cluster0.sqkox39.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
db = client["meubanco"]
collection = db["minhacolecao"]

#Gerando chave Fernet
key = Fernet.generate_key()
fernet = Fernet(key)

print("Bem-Vindo ao chat\n")
nome=input("Insira seu nome de usuário:\n")
collection.insert_one({'nome':nome})
mensagem=""
mensagem[0]=input("Insira sua primeira mensagem:\n")
while mensagem!="":
    for i in range(0,mensagem.lenght()):
     print("="*20)
     mensagem[i]=input("=>\n")
     print("="*20)
     #criptografia da mensagem em mensagem_cripto = @string, usando fernet.encode()  
     mensagem_cripto=fernet.encrypt(mensagem.encode())
     #inserção da mesagem
     collection.insert_one({'mensagem_crip':mensagem_cripto})

resposta=input("deseja recuperar uma mensagem:\n")
if resposta=="s":
   nome=input("Insira o nome do usuário:\n")
collection.find_one({"nome":nome})
resultado = collection.find_one({"mensagem_crip": mensagem_cripto})
mensagem_recuperado_criptografado = resultado["mensagem_crip"]
mensagem_descripto=fernet.decrypt()
valor_descriptografado = fernet.decrypt(mensagem_recuperado_criptografado).decode()
print(f"Valor descriptografado: {mensagem_descripto}")




