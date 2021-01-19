import Decrypter

# CreateRotor(self, alphabet = string.ascii_lowercase)
# SetRotorTo(self, letter ,Alphabet = string.ascii_lowercase)
# RotateRotor(self, num ,Alphabet = string.ascii_lowercase)
#
# SubstitutionCipher(self, alphabetCipherText , alphabetPlainText = string.ascii_uppercase):
# CaesarCipher(self, shift = 3) YKHIORFVGO
# VigenereCipher(self, password = 'a')
message = "LOREM IPSUM"
machine = Decrypter.Ciphers(message)

print(''.join(machine.VigenereCipher('LATIM')))


