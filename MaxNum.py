class Maxnum:
    def __init__(self):
        self.n=int(input())
        self.narr=input()
        self.narr=[int(i) for i in (self.narr).split(" ")]

    def FMax(self):
        (self.narr).sort()
        print((self.narr)[len(self.narr)-1])

m=Maxnum()
m.FMax()
