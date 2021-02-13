print("Please enter you ID code:")
#isikukood = input(int())
isikukood = "38803160272"
birthdate = isikukood[1:7]
gender = isikukood[0]
birth_year = isikukood[1:3]
birth_month = isikukood[2:5]
birth_day = isikukood[5:7]

if int(len(isikukood)) == 11:  # ID length checker
    print("ID length check:\nPASSED")
else:
    print("ID length check:\nFAILED")

# ID sex checker
print("ID code gender check:\n....................")
if int(gender) % 2 == 0:
    gender_id = ("Female")
    print("Gender check: PASSED\n" + gender_id)
else:
    gender_id = ("Male")
    print("Gender check: PASSED\n" + gender_id)

if gender == 1 or gender == 2:
    century = ("18")
    elif gender == 3 or gender == 4:
        century = ("19")
        elif gender == 5 or gender == 6:
            century = ("20")
            elif gender == 7 or gender == 8:
                century = ("21")
            else:
                century = ("22")
            print("Your birth date is:" + birth_day + (".") + birth_month + (".") + century + birth_year)