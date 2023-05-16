country = str(input('Введите название страны: '))
cost = int(input('Введите цену: '))
if country == 'Япония' or country == 'Китай':
    cost = cost - cost*8/100
elif country == 'США' or country == 'Тайвань':
    cost = cost + cost*14/100
print (f'Новая цена равна условных {cost} единиц')