revenue = int(input("Введите значение выручки: "))
cost = int(input("Введите значение издержек: "))

if revenue > cost:
    profit = revenue - cost
    print(f"Компания работает с прибылью: {profit}")
    print(f"Рентабельность: {profit / revenue:.2}")
    staff_count = int(input("Введите количество сотрудников: "))
    print(f"Прибыль в рассчете на 1 сотрудника: {profit / staff_count}")
else:
    print("Компания работает в минус!!!")