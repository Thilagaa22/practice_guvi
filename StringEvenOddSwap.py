class StrEvenoddswap:
    def __init__(self):
        self.inp=input()

    def StringSwap(self):
        inplist=list(self.inp)
        for i in range(0,len(inplist),2):
            if(i==len(inplist)-1):
                break
            else:
                inplist[i],inplist[i+1]=inplist[i+1],inplist[i]
        self.inp="".join(inplist)
        print(self.inp)

s=StrEvenoddswap()
s.StringSwap()

    
