a = int(input('Введите первоночальную стоимость вклада: '))
b = int(input('Введите роцентную ставку: '))
c = int(input('Введите количество периодов начисления ставки: '))
d = int(input('Введите общий срок вклада в годах: '))
hard = round(a*(1+b/(c*100))**(c*d), 2)
simple =round(a*(1+b*c/100), 2)
print(f'Накопленная стоимость по формуле сложноых процентов равна {hard} рублей')
print(f'Накопленная стоимость по формуле простых процентов равна {simple} рублей')
print(f'Разница составляет {round(hard-simple,2)} рублей')