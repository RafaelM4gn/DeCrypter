import string

class Ciphers:
    def __init__(self, message):
        self.message = list(message)

    ''' ---ROTORS---'''
    def CreateRotor(self, alphabet = string.ascii_uppercase):
        newAlphabet = alphabet
        return newAlphabet

    def SetRotorTo(self, letter ,Alphabet = string.ascii_uppercase):
        newAlphabet = []
        for x in range(26, 0, -1):
            newAlphabet.append(Alphabet[Alphabet.index(letter) - x])
        return newAlphabet

    def RotateRotor(self, num ,Alphabet = string.ascii_uppercase):
        return Alphabet[num:] + Alphabet[:num]

    ''' ---CIPHERS--- '''
    def SubstitutionCipher(self, alphabetCipherText , alphabetPlainText = string.ascii_uppercase):
        for x in range(len(self.message)):
            if self.message[x] != ' ':
                self.message[x] = alphabetCipherText[alphabetPlainText.index(self.message[x].upper())]
        return self.message

    def CaesarCipher(self, shift = 3):
        self.message = self.SubstitutionCipher(self.RotateRotor(shift))
        return self.message

    def VigenereCipher(self, password = 'A'):
        if len(password) <= len(self.message):
            z = 0
            for x in range(len(self.message) - len(password)):
                password += password[x]
            for y in range(len(password)):
                if self.message[y] == ' ':
                    y += 1
                else:
                    alphabet = self.SetRotorTo(password[z])
                    self.message[y] = alphabet[string.ascii_uppercase.index(self.message[y].upper())]
                    z += 1
        return self.message