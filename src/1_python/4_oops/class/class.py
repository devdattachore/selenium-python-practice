class Calculator:
    num = 100

    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2
        print("Inside constructor")

    def addIntegers(self):
        return self.num1 + self.num2 + Calculator.num


obj = Calculator(21, 23)
print(obj.num)
print(obj.addIntegers()
      )
