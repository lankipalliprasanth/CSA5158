import hashlib
text = hashlib.sha1(b'Hello')
encrypt = text.hexdigest()
print(encrypt)
