import math
x = int(input('x = '))
t = int(input('t = '))
print(f'y = {round((8*math.pi*t+5*math.sin(x))/(math.sqrt(t)-abs(math.cos(2*x))), 2)}')