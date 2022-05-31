import hashlib

result = hashlib.md5(b"Hello MD5").hexdigest()
print(result)

result = hashlib.md5("Hello MD5".encode("utf-8")).hexdigest()
print(result)

m = hashlib.md5(b"Hello MD5")
print(m.name)
print(m.digest_size) # 16 bytes (128 bits)
print(m.digest())    # bytes
print(m.hexdigest()) # bytes in hex representation
