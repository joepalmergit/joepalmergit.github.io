from argon2 import PasswordHasher
from argon2.exceptions import VerifyMismatchError

ph = PasswordHasher()

def hash_password(password):
    hashed = ph.hash(password)
    return hashed

def check_password(password, hashed_password):
    try:
        ph.verify(hashed_password, password)
        return True
    
    except VerifyMismatchError:
        return False
