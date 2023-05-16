def product(a, b):
    return 3*a**2+b-4
a=int(input('Введите значение a: '))
b=int(input('Введите значение b: '))
print(f"Значение функции = {product(a,b)}")
print(f"c = {round(product(a,b)+a%b)}")