import hashlib
import secrets

# Gere um salt aleatorio, usando o modelo secrets

salt = secrets.token_hex(16)
print(salt)

# Definir uma senha

password = "Bolinhas"

# Hash para a senha, usando o salt e o algoritmo SHA-256

hash_object = hashlib.sha256((password + salt).encode())

hash_hex = hash_object.hexdigest()
print(hash_hex)