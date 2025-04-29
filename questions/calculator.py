class BasicCalculator:

    def __init__(self, number1, number2):
        self.number1 = number1
        self.number2 = number2

    def addition(self):
        suma = self.number1 + self.number2
        print(f"Addition: {self.number1} + {self.number2} = {suma}")

    def subtraction(self):
        rest = self.number1 - self.number2
        print(f"Subtraction: {self.number1} - {self.number2} = {rest}")

    def multiplication(self):
        mult = self.number1 * self.number2
        print(f"Multiplication: {self.number1} * {self.number2} = {mult}")

    def division(self):
        div = self.number1 / self.number2
        print(f"Division: {self.number1} / {self.number2} = {div}")


calculator = BasicCalculator(10, 5)
calculator.addition()
calculator.subtraction()
calculator.multiplication()
calculator.division()
