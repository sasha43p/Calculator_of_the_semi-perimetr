import math
first = float(input ("Введите первую сторону"))
second = float(input ("Введите вторую сторону"))
third = float(input ("Введите третью сторону"))
if first<0 or second<0 or third<0 or first+second<0 or first+third<0 or second+third<0:
    print ("это так не работает")
else:
    perimeter = (first+second+third) / 2
    semi_perimeter = (perimeter*(perimeter-first)*(perimeter-second)*(perimeter-third))**0.5
    print ("Площадь треугольника равна:", semi_perimeter)