print ('Цей код порівнює два цілі числа введені з клавіатури і виводить "числа рівні" або числа у порядку зростання якщо рівність не справджується')

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

if number1==number2:
    print('числа рівні')
elif number1>number2:
    print(number1, number2)
else:
    print(number2, number1)