from flask import Flask,render_template, request, jsonify
from cipher.caesar import CaesarCipher
from cipher.vigenere import VigenereCipher
from cipher.railfence import RailFenceCipher
from cipher.playfair import PlayFairCipher
from cipher.transposition import TranpositionCipher

app = Flask(__name__)
CIPHER_CLASSES = {
    "caesar": CaesarCipher,
    "vigenere": VigenereCipher,
    "railfence": RailFenceCipher,
    "playfair": PlayFairCipher,
    "transposition": TranpositionCipher
}
@app.route("/")
def home():
    return render_template("index.html")

@app.route("/<cipher_name>")
def cipher(cipher_name):
    return render_template("cipher.html", cipher_name=cipher_name)

@app.route("/<cipher_name>/encrypt", methods=["POST"])
def encrypt(cipher_name):
    text = request.form['inputPlainText']
    key = request.form['inputKeyText']
    error = None

    if cipher_name in ["vigenere", "playfair"] and not key.isalpha():
        error = "Key must contain only letters for this cipher."
        return render_template("cipher.html", cipher_name=cipher_name, error=error, inputCipherText=text, inputKeyCipher=key)
    elif not cipher_name in ["vigenere", "playfair"] and not key.isdigit():
        error = "Key must contain only numbers for this cipher."
        return render_template("cipher.html", cipher_name=cipher_name, error=error, inputCipherText=text, inputKeyCipher=key)

    try:
        key = int(key)
    except ValueError:
        pass
    CipherClass = CIPHER_CLASSES.get(cipher_name)

    if not CipherClass:
        error = "Cipher not supported"
        return render_template("cipher.html", cipher_name=cipher_name, error=error)
    
    cipher = CipherClass()
    if cipher_name == "playfair":
        matrix = cipher.create_playfair_matrix(key)
        encrypted_text = cipher.encrypt_text(text, matrix)
    else:
        encrypted_text = cipher.encrypt_text(text, key)
    return f"text: {text}<br/>key: {key}<br/>encrypted text: {encrypted_text}"

@app.route("/<cipher_name>/decrypt", methods=["POST"])
def decrypt(cipher_name):
    text = request.form['inputCipherText']
    key = request.form['inputKeyCipher']
    error = None

    if cipher_name in ["vigenere", "playfair"] and not key.isalpha():
        error = "Key must contain only letters for this cipher."
        return render_template("cipher.html", cipher_name=cipher_name, error=error, inputPlainText=text, inputKeyText=key)
    elif not cipher_name in ["vigenere", "playfair"] and not key.isdigit():
        error = "Key must contain only numbers for this cipher."
        return render_template("cipher.html", cipher_name=cipher_name, error=error, inputCipherText=text, inputKeyCipher=key)
    
    try:
        key = int(key)
    except ValueError:
        pass

    CipherClass = CIPHER_CLASSES.get(cipher_name)
    if not CipherClass:
        error =  "Cipher not supported"
        return render_template("cipher.html", cipher_name=cipher_name, error=error)
    
    cipher = CipherClass()
    if cipher_name == "playfair":
        matrix = cipher.create_playfair_matrix(key)
        decrypted_text = cipher.decrypt_text(text, matrix)
    else:
        decrypted_text = cipher.decrypt_text(text, key)
    return f"text: {text}<br/>key: {key}<br/>decrypted text: {decrypted_text}"


# @app.route("/caesar")
# def caesar():
#     return render_template("caesar.html")

# @app.route("/encrypt", methods=["POST"])
# def encrypt():
#     text = request.form['inputPlainText']
#     key = int(request.form['inputKeyText'])
#     Caesar = CaesarCipher()
#     encrypted_text = cipher.encrypt_text(text, key)
#     return f"text: {text}<br/>key: {key}<br/>encrypted text: {encrypted_text}"

# @app.route("/decrypt", methods=["POST"])
# def decrypt():
#     text = request.form['inputCipherText']
#     key = int(request.form['inputKeyCipher'])
#     Caesar = CaesarCipher()
#     decrypted_text = Caesar.decrypt_text(text, key)
#     return f"text: {text}<br/>key: {key}<br/>decrypted text: {decrypted_text}"

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)