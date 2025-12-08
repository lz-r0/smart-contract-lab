# -----------------------------------------
# Minimal SHA-256 hashing example (Python)
# -----------------------------------------
# Purpose:
#   - Show how to import hashlib
#   - Demonstrate SHA-256 hashing of a byte string
# -----------------------------------------


import hashlib
# hashlib includes SHA-256, SHA-1, MD5, etc.

digest = hashlib.sha256(b"hello").hexdigest()
# Compute SHA-256 of the byte string b"hello"


print(digest)
