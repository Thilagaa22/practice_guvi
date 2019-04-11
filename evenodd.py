class checkval:
    def __init__(self):
        self.num=int(input())
    def checkng(self):
        if(self.num<0):
           print("invalid")
        elif(self.num%2==0):
              print("Even")
        else:
               print("Odd")
               
c1=checkval()
c1.checkng()
