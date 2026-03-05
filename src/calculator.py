class Calculator:
    def __init__(self):
        self.result = 0

    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        if b == 0:
            raise ValueError("Cannot divide by zero")
        return a / b

    def clear(self):
        self.result = 0
        return self.result


if __name__ == "__main__":
    calc = Calculator()
    print("Quick-Calc CLI")
    print("Example: 2 + 3")
    a = float(input("First number: "))
    op = input("Operator (+, -, *, /): ")
    b = float(input("Second number: "))

    if op == "+":
        print("Result:", calc.add(a, b))
    elif op == "-":
        print("Result:", calc.subtract(a, b))
    elif op == "*":
        print("Result:", calc.multiply(a, b))
    elif op == "/":
        try:
            print("Result:", calc.divide(a, b))
        except ValueError as e:
            print("Error:", e)
    else:
        print("Invalid operator")
