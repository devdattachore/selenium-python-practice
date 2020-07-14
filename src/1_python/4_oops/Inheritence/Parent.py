class Parent:
    num = 100

    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2
        print("Inside parent constructor")

    def addIntegers(self):
        return self.num1 + self.num2 + Parent.num