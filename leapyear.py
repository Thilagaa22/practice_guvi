class lpyear:
    def __init__(self):
        self.year= int(input())
    def findl(self):
        if((self.year)%4==0 and (self.year)%100!=0):
            print("yes")
        else:
            print("no")

lp= lpyear()
lp.findl()
