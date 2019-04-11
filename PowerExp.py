class powerexpr:
    def __init__(self):
        self.nkarr=input()
        self.nkarr=(self.nkarr).split(" ")
        self.nkarr=[int(i) for i in self.nkarr]
    def cal(self):
        mul=1
        for i in range(0,self.nkarr[1]):
            mul=mul*self.nkarr[0]
        print(mul)

p= powerexpr()
p.cal()
