side_a, side_b, side_c = input('Please enter 3 sides of triangle: ').split(',') #разделение переменных
#a, b, c, d, = 1, 2, 3, 4,
#print(side_a)
#print(side_b)
#print(side_c)

half_perimeter = (float(side_a) + float(side_b) + float(side_c)) / 2
print(half_perimeter)

triangle_square = (half_perimeter * (half_perimeter - float(side_a)) * (half_perimeter - float(side_b) * (half_perimeter - float(side_c))) ** 0.5
print(triangle_square)
