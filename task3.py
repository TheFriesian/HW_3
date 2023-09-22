'''
3. Користувач вводить два числа та матем дію: + - * або /
'''

valid_operations = {'+', '-', '*', '/'}

while True:
    try:
        number1 = int(input("Введіть перше число: "))
        break
    except ValueError:
        print("Будь ласка, введіть коректне ціле число.")


while True:
    try:
        number2 = int(input("Введіть друге число: "))
        break
    except ValueError:
        print("Будь ласка, введіть коректне ціле число.")


while True:
    operation = input("Введіть математичну дію (+ - * /): ")
    if operation in valid_operations:
        break  # Exit the loop if a valid operation is entered
    else:
        print("Будь ласка, введіть одну з допустимих операцій: + - * /")

if operation == '+':
    result = number1 + number2
elif operation == '-':
    result = number1 - number2
elif operation == '*':
    result = number1 * number2
elif operation == '/':
    if number2 != 0:
        result = number1 / number2
    else:
        result = "Ділення на нуль не допустиме"

print("Результат: ", result)