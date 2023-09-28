from cryptography.fernet import Fernet

#Cria a chave contendo o
def gera_chave():
    return Fernet.generate_key()

def encriptar_mensagem(mensagem, chave):
    cifra_chave = Fernet(chave)
    encripta = cifra_chave.encrypt(mensagem.encode())
    return encripta

def decripta_mensagem(mensagem, chave):
    cifra_chave = Fernet(chave)
    decripta = cifra_chave.decrypt(mensagem.decode())
    return decripta

chave = gera_chave()
mensagem = str(input('Entre com a mensagem a ser criptografada: '))
encriptado = encriptar_mensagem(mensagem, chave)
decriptado = decripta_mensagem(encriptado, chave)

print(chave)
print(encriptado)
print(decriptado)