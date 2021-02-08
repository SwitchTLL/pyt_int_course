some_string = "Hello world"

print(some_string.replace(some_string[4:8], ""))  # Symbol replace from 4 to 8

print(some_string.replace("world", "people"))  # replace word "world" to "people"
print(some_string)

some_string = some_string.replace("world", "people")
print(some_string)