#!/usr/bin/python3

''' Server Response:

* Connected to 192.150.144.3 (192.150.144.3) port 80 (#0)

< WWW-Authenticate:
    Digest realm="Private"
    nonce="vi3itvuLBQA=8ad9bd8ddb43a2ba1946786c3aa4a49eec1236e0"
    algorithm=MD5
    qop="auth"

'''

# How is digest calculated?
# hash1 = md5(username:realm:password)
# hash2 = md5(method:uri)
# response = hash1:nonce:hash2

import hashlib
hash1 = hashlib.md5('bob:Private:<get_password_lisg>')
hash2 = hashlib.md5('GET:/poc/')


