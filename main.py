calculator_logo = '''

 _____________________
|  _________________  |
| | JO  3.141592654 | |
| |_________________| |
|  __ __ __ __ __ __  |
| |__|__|__|__|__|__| |
| |__|__|__|__|__|__| |
| |__|__|__|__|__|__| |
| |__|__|__|__|__|__| |
| |__|__|__|__|__|__| |
| |__|__|__|__|__|__| |
|  ___ ___ ___   ___  |
| | 7 | 8 | 9 | | + | |
| |___|___|___| |___| |
| | 4 | 5 | 6 | | - | |
| |___|___|___| |___| |
| | 1 | 2 | 3 | | x | |
| |___|___|___| |___| |
| | . | 0 | = | | / | |
| |___|___|___| |___| |
|_____________________|

'''
print(calculator_logo)
def add(n1,n2):
    return n1 + n2
def subtract(n1,n2):
    return n1 - n2
def multiply(n1,n2):
    return n1 * n2
def divide(n1,n2):
    if n2 == 0:
        return "Error Division by zero"
    return n1 / n2
operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}
def calculator():
    first_number = float(input("What is the first number? "))
    while True:
        for operator in operations:
            print(operator)
        symbol = input("Pick an operator: ")
        if symbol not in operations:
            print("Invalid operator:\nTry again")
            return
        second_number = float(input("What is the second number? "))
        output = operations[symbol](first_number,second_number)
        print(f"{first_number} {symbol} {second_number} = {output}")
        options = input(f"Type 'yes' to continue calculating with {output},type 'new' to start a new calculation, or type exit to stop the game:\n")
        if options == "yes":
            first_number = output
        elif options == "new":
            print("\n" * 100)
            calculator()
        elif options == "exit":
            return
        else:
            print("Invalid input:\nTry again!")
calculator()
























