# Завдання 2.
#Користувач вводить з клавіатури якусь кількість метрів.
#Залежно від вибору користувача, програма конвертує метри
#в милі, дюйми або ярди.

x = int(input('Введіть кількість метрів: '))
y = int(input('1. Щоб конвертувати в милі натисніть 1. '
              '\n2. Щоб конвертувати в дюйми натисніть 2. '
              '\n3. Щоб конвертувати в ярди натисніть 3. '
              '\n'))
if y == 1:
    print(x, 'м рівне: ', x*0.000621, 'милі,')
elif y == 2:
    print(x, 'м рівне: ', x*39.370, 'дюйма,')
elif y == 3:
    print(x, 'м рівне: ', x * 1.0936, 'ярда,')