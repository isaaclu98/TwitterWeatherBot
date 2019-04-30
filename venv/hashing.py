import uuid
import hashlib


def hashText(text):
    """
        Basic hashing function for a text using random unique salt.
    """
    salt = "vrk1o38avzupijig6t0s4k20yewigchj"
    return hashlib.sha256(salt.encode() + text.encode()).hexdigest() + ':' + salt


def matchHashedText(hashedText, providedText):
    """
        Check for the text in the hashed text
    """
    _hashedText, salt = hashedText.split(':')
    print(_hashedText)
    return _hashedText == hashlib.sha256(salt.encode() + providedText.encode()).hexdigest()

matchHashedText(AEAB35EB683B17D027D5CB65582E6191C14F838ADB3E75807E11810DAFA2AFBC,"isaac")