

nombre = 3.14

if __name__ == "__main__":
    print("BEGIN VariableFloat.py")
    print(type(nombre))

    quotient = nombre // 2  # division entiere
    print(quotient, type(quotient))
    quotient = nombre / 2  # division réelle
    print(quotient, type(quotient))
    quotient = nombre % 2  # modulo
    quotient2 = nombre - (nombre // 2) * 2
    print(quotient, type(quotient))
    print(quotient2, type(quotient2))
