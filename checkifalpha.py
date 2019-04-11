class Alph:
    def __init__(self):
        self.alphabets="abcdefghijklmnopqrstuvwxyz"
        self.inp=input()
    def checkalph(self):
        if(self.inp in self.alphabets):
            print("Alphabet")
        else:
            print("No")

a1= Alph()
a1.checkalph()
