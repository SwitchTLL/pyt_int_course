# courses = ["History", "Math", "Programming", "Physics", "art", "Programming", "chemistry", "123", "534"]
# numbers = [1, 45, 63, 34, 56, 78, 3]
# courses2 = ["Art", "Biology"]
# print(courses)
# courses.insert(2, "Biology")
# print(courses)
#
# courses.extend(courses2)
# print(courses)
#
# print(numbers)
# numbers.sort()
# print(numbers)
#
# print(courses)
# courses.sort()
# print(courses)
# courses.sort(reverse=True)
# print(courses)
#
# option = True
# numbers.sort(reverse=option)
# print(numbers)
#
# print(sorted(courses))
# print(courses)
#
# print(sorted(numbers))
# print(numbers)
# print(min(numbers))
# print(max(numbers))
# print(min(courses))
# print(max(courses))
# print(sum(numbers))
# print(courses.index("Math"))
# print(courses)
# math_index = courses.index("Math")
# print(courses[math_index])
# print("art" in courses)
# if "art" in courses:
#     print("GOOD")
# else:
#     print("BAD")
# print(45 in numbers)
# new_string = " @#$* ".join(courses)
# print(new_string)
# print(type(new_string))
#
# new_list = new_string.split("\n")
# print(new_list)
# print(type(new_list))
# list_1 = ['Math', 'History', 'Programming', 'Physics']
# list_2 = list_1.copy()
# print(list_1)
# print(list_2)
#
# list_1[2] = 'Sports'
# list_2[0] = 'Art'
#
# print(list_1)
# print(list_2)
# new_courses = courses + courses2
#
# print(new_courses)
# courses = ("Math", "History", "Programming", "Physics")
# variable = 10
# courses2 = ("Art", variable)
#
# print(courses2)
#
# variable = 16
# print(courses2)
# set1 = {"Math", "History", "Programming", "Physics", "Math"}
# set2 = {"Art", "Physics", "Design", "History"}
#
# list1 = ["Math", "History", "Programming", "Physics", "Math", "History"]
# print(list1)
# print(type(list1))
# print(list(set(list1)))

#set1 = {"Math", "History", "Programming", "Physics", "Math"}
#set2 = {"Art", "Physics", "Design", "History"}

# # intersection() method returns a set of intersection between two sets
# print(set1.intersection(set2))
#
# # difference() method returns a set of differences in two sets
# print(set2.difference(set1))
# print(set1.difference(set2))

# union() method will return a set of all values from both sets
# print(set1.union(set2))
# courses = ["Math", "History", "Programming", "Physics", "Art", "Biology"]
# #courses = "Hello world"
# counter = 0
# for subject in courses:
#     print(subject)
#     counter += 1
# print(counter)

courses = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# courses - "Hello world"
counter = 0
for num1 in courses:
    for num2 in courses:
        for num3 in courses:
            for num4 in courses:
                print(num1, num2, num3, num4)