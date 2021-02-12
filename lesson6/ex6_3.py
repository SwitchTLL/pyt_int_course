def double(number):
    result = number * 2
    return result

def triple(number):
    result = number * 3
    return result

def create_string(name):
    result = 'Hello ' + name
    return result

print(create_string('Roman') + ', How are you?')

print(double(5))
print(triple(5))

double_five = double(5)
print(double_five)
print(type(double_five))

print(double(5) + triple(7))

