import base64
from hashlib import sha256

def generate_key(pin):
    return sha256(pin.encode()).digest()

def encrypt_report(data_string, pin):
    encoded = base64.b64encode(data_string.encode()).decode()
    return f"CCC_LOCKED_{encoded}"

def decrypt_report(encrypted_string, pin):
    if not encrypted_string.startswith("CCC_LOCKED_"):
        return "Format Error"
    encoded = encrypted_string.replace("CCC_LOCKED_", "")
    return base64.b64decode(encoded).decode()
