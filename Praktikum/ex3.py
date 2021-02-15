side_a = float(input("Please enter side A:"))
side_b = float(input("Please enter side B:"))
side_c = side_a + side_b
print(side_c)
if side_a * side_a + side_b * side_b == side_c * side_c:
    print("This triangle is right")
else:
    print("This triangle is NOT right")