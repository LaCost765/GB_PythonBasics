seconds = int(input("Введите время в секундах: "))
hours, minutes, seconds = (seconds // 3600, (seconds % 3600) // 60, (seconds % 3600) % 60)

if hours < 10:
    hours = f'0{hours}'
if minutes < 10:
    minutes = f'0{minutes}'
if seconds < 10:
    seconds = f'0{seconds}'
    
print(f'{hours}:{minutes}:{seconds}')