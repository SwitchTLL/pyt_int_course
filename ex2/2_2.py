side_a, side_b, side_c = input('Please enter 3 sides of triangle: ').split(',')
# .split(',') разделитель переменных при вводе значений. прим.: a, b, c, d, = 1, 2, 3, 4,

print(side_a)
print(side_b)
print(side_c)

semiPerim = (float(side_a) + float(side_b) + float(side_c)) / 2
# p=P/2=(abc)/2 - полупериметр треугольника

print(semiPerim)

trArea = (semiPerim * (semiPerim - float(side_a)) * (semiPerim - float(side_b) * (semiPerim - float(side_c)))) ** 0.5
# areaTr = S=√p(p-a)(p-b)(p-c) - формула Герона
print("Triangle area is", trArea)
