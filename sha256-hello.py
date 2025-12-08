# About: Minimal SHA-256 hashing example (in Python).



import hashlib  # includes SHA-256, SHA-1, MD5

print(hashlib.sha256(b"hello").hexdigest())

