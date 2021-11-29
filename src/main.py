class Calc:
    def __init__(self):
        self.num1 = 0
        self.num2 = 0

    def operation(self):

        while True:
            print("Choose wich mathemtical operation you wan to run:")
            print("Sum - press +")
            print("Minus - press -")
            print("Devide - press /")
            print("Multiply - press *")

        
            choice = str(input())

            print("Which numbers?")
            self.num1 = int(input("num1:"))
            self.num2 = int(input("num2:"))

            if choice == "+":
                print(self.plus())
    
            if choice == "-":
                print(self.minus())
    
            if choice == "/":
                print(self.devide())
    
            if choice == "*":
                print(self.multiply())


    def plus(self):
        result = self.num1 + self.num2
        return result

    def minus(self):
        result = self.num1 - self.num2
        return result

    def devide(self):
        result = self.num1 / self.num2
        return result

    def multiply(self):
        result = self.num1 * self.num2
        return result


if __name__ == "__main__":
    calc = Calc()
    calc.operation()