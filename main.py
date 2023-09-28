#pip install cryptography
from cryptography.fernet import Fernet

def generate_key():
    """
    Gera uma chave de criptografia aleatória
    """
    return Fernet.generate_key()

def encrypt_message(message, key):
    """
    Criptografa uma mensagem usando a chave fornecida
    """
    cipher_suite = Fernet(key)
    encrypted_message = cipher_suite.encrypt(message.encode())
    return encrypted_message

def decrypt_message(encrypted_message, key):
    """
    Descriptografa uma mensagem usando a chave fornecida
    """
    cipher_suite = Fernet(key)
    decrypted_message = cipher_suite.decrypt(encrypted_message).decode()
    return decrypted_message.encode()

key = generate_key()
message = str(input('Digite sua mensagem: '))
encrypted_message = encrypt_message(message, key)
decrypted_message = decrypt_message(encrypted_message, key)

print("Mensagem original:", message)
print("Mensagem criptografada:", encrypted_message)
print("Mensagem descriptografada:", decrypted_message)