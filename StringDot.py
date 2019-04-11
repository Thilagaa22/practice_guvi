from string import punctuation as p
class Stringdot:
    def __init__(self):
        self.str=input()
    def addDot(self):
        for i in range(0,len(p)):
            if(p[i]=="."):
                print(self.str+p[i])
                break

s=Stringdot()
s.addDot()
