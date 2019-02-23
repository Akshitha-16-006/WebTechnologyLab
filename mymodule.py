class Calculator(object):
    def __init__(self,num1=0.0,num2=0.0):
        self.num1=num1
        self.num2=num2

    def add(self):
        return (self.num1+self.num2)
    def sub(self):
        return (self.num1-self.num2)
    def div(self):
        return (self.num1/self.num2)
    def mul(self):
        return (self.num1*self.num2)
    
