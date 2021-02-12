# Тип скобок для этих комманд критичен!

# LIST[] - изменяемый
# TUPLE() - не изменяемый
# DICT{} -
# SET{} - frozen

empty_string = ""
print(type(empty_string))

empty_list = []
print(type(empty_list))  # empty_list = [1234, 1234.56, "some string", True, None, [1234,"new_string", False]]
# print(some_list)
# print(some_list[0:3])

empty_tuple = ()
print(type(empty_tuple))

empty_set = {}
print(type(empty_set))

some_list = [1234, 1234.56, "some string", True, None, [1234,"new_string", False]]
print(some_list)

print(some_list[0:3])

print(some_list[5])

courses = ["History", "Math", "Literature", "Physics", "Programming", [1, 3, 4, 6, 7,]]
print(courses)
courses[2] = "Art"
print(courses[5][4])  # Список внутри списка
courses[2] = "Litera"
print(courses)

print(len(courses[5]))
courses2 = ["Art", "Biology",]
print(courses + courses2)

courses.append("Art")
print(courses)

courses[5].append(courses2)
print(courses2[5] [5] [1])

courses.remove("Math")
print(courses)

courses = ["History", "Math", "Literature", "Physics", "Programming", ]
courses2 = ["Art", "Biology"]
print(courses)

#courses.remove("Math")
#print(courses)

courses.pop()
print(courses)

popped_item = courses.pop()
popped_item2 = courses.pop()
print(courses)
print(popped_item)
print(popped_item2)

courses = ["History", "Math", "Literature", "Physics", "Programming", ]
courses2 = ["Art", "Biology"]

print(courses)
courses.insert(2, "Biology")
print(courses)