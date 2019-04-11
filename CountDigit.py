class countnodigit:
    def __init__(self):
        self.numchar=input()
    def countdig(self):
        countnum=0
        num=int(self.numchar)
        while(num>0):
            if(num%10>=0):
                countnum=countnum+1
                num=int(num/10)
        print(countnum)

cd=countnodigit()
cd.countdig()
