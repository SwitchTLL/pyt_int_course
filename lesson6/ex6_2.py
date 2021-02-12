# # Ссылки на строки кода
#
# def squares():
#     #print('Hello world!')
#     x = 5
#     print(x)
#
# squares()

def squares(number, multiplier):
    result = number ** multiplier
    return result

x = 5
y = 3

#
# print(squares(x, y,))
# print(type(squares(x, y)))
squares(x,y)
print(squares(x,y) *10)

a, b, c, = input("Please enter anything: ").split("*")
print(a, b, c)


