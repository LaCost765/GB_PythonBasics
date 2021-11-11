n = int(input("Введите число: "))
max_digit = n % 10
n //= 10
while n > 0:
    if (n % 10) > max_digit:
        max_digit = n % 10
    n //= 10
print(f'Максимальная цифра в введенном числе: {max_digit}')