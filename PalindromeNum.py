class palindro:
    def __init__(self):
        self.N=int(input())
    def palindrotest(self):
        rev=0
        temp=self.N
        while(temp!=0):
            rev=rev*10
            rev=rev+ (temp%10)
            temp=temp//10
        if(rev==self.N):
            print("yes")
        else:
            print("no")

p=palindro()
p.palindrotest()
        
