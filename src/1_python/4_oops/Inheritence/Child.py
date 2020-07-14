from Parent import Parent


class Child(Parent):
    childNum = 200;

    def __init__(self, num1, num2):
        Parent.__init__(self, num1, num2)
        print("inside child constructor")

    def getAllNums(self):
        return Child.childNum + self.addIntegers()


obj = Child(2, 9);
print(obj.childNum)
print(obj.getAllNums())