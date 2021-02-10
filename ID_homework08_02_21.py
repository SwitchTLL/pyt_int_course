import sys,time

# def sprint(str):
#    for c in str + '\n':
#      sys.stdout.write(c)
#      sys.stdout.flush()
#      time.sleep(0.05)

print("Please enter you ID code:")
#isikukood = input(int())
isikukood = "32705300372"
birthdate = isikukood[1:7]

if int(len(isikukood)) == 11:  #ID length checker
    print("ID length check:\nPASSED")
else:
    print("ID length check:\nFAILED")

# ID sex checker
num_id = list(isikukood)
#print(num_id)
gender = int(num_id[0])
#print(sex)
num_id2 = list(isikukood)
#print(num_id2)

print("ID code gender check:")
if (gender % 2 == 0):
    print("Gender check:\nFEMALE")
else:
    print("Gender check:\nMALE")

birth_year = birthdate[1:3]
birth_month = birthdate[2:5]
birth_day = birthdate[5:7]

print(gender)

if gender == 1 or gender == 2:
    century = ("18")
    if gender == 3 or gender == 4:
        century = ("19")
        if gender == 5 or gender == 6:
            century =("20")
            if gender == 7 or gender == 8:
                century = ("21")
    print("Birthyear is " + century + birth_year)