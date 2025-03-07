import hashlib

my_string = "Olá mundo"
hash_objeto = hashlib.md5(my_string.encode())
print(hash_objeto.hexdigest())

hash_sha1 = hashlib.sha1(my_string.encode())
print(hash_sha1.hexdigest())

hash_sha256 = hashlib.sha256(my_string.encode())
print(hash_sha256.hexdigest())

hash_sha512 = hashlib.sha512(my_string.encode())
print(hash_sha512.hexdigest())