

def hello():
    print("Hello!")
    pass

def random_number():
    return 0


def multiply(a : int, b: int)->int:
    return a * b

if __name__ == "__main__":
    print("BEGIN Functions.py")
    print(hello())
    n = random_number()
    print("n =", n)
    result = multiply(5, 2)
    print("multiply(2, 5) =", result)
