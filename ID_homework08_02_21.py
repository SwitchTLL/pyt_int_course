print("Please enter you Estonian ID code:")
eeid = input()
#eeid = "38803160272"
bth_date = eeid[1:7]
gender = eeid[0]
bth_year = eeid[1:3]
bth_month = eeid[3:5]
bth_day = eeid[5:7]
birth_region = int(eeid[7:10])
int_eeid = int(eeid)

if int(len(eeid)) == 11:  # ID length checker
    print("ID length check:\nPASSED")
else:
    print("ID length check:\nFAILED")

# ID gender checker
print("ID code gender check:")
if int(gender) % 2 == 0:
    print("Gender check: PASSED\nFEMALE")
else:
    print("Gender check: PASSED\nMALE")
    gender = str(int(gender))
# Birth century checker
if gender == "1" or gender == "2":
    century = "18"
elif gender == "3" or gender == "4":
    century = "19"
elif gender == "5" or gender == "6":
    century = "20"
elif gender == "7" or gender == "8":
    century = "21"
elif gender == "9" or gender == "0":
    century = "22"


print("Your birthdate is: " + bth_day + "." + bth_month + "." + century + bth_year)  # Birth date output
print(int(gender) % 2)

# Region control
if birth_region in range(1,11):
    print('You were born in Kuressaare haigla')
elif birth_region in range(11, 20):
    print("You were born in Tartu Ülikooli Naistekliinikum")
elif birth_region in range(20, 151):
    print('You were born in Ida-Tallinna keskhaigla, Pelgulinna sünnitusmaja (Tallinn)')
elif birth_region in range(150, 159):
    print('You were born in Keila haigla')
elif birth_region in range(160, 219):
    print('You were born in Rapla haigla, Loksa haigla, Hiiumaa haigla (Kärdla)')
elif birth_region in range(220, 269):
    print('You were born in Ida-Viru keskhaigla (Kohtla-Järve, endine Jõhvi)')
elif birth_region in range(270, 369):
    print('You were born in Maarjamõisa kliinikum (Tartu), Jõgeva haigla')
elif birth_region in range(370, 419):
    print('You were born in Narva haigla')
elif birth_region in range(420, 469):
    print('Maarjamõisa kliinikum (Tartu), Jõgeva haigla')
elif birth_region in range(470, 489):
    print('Haapsalu haigla')
elif birth_region in range(490, 519):
    print('Järvamaa haigla (Paide)')
elif birth_region in range(520, 569):
    print('Rakvere haigla, Tapa haigla')
elif birth_region in range(570, 599):
    print('Valga haigla')
elif birth_region in range(600, 649):
    print('Viljandi haigla')
elif birth_region in range(650, 699):
    print('Lõuna-Eesti haigla (Võru), Põlva haigla')

# ID code checksum validation

test_list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 1]
test_list2 = [3, 4, 5, 6, 7, 8, 9, 1, 2, 3]

counter = 0
index_counter = 0

for digit in test_list1:
    counter = counter + digit * int(eeid[index_counter])
    index_counter += 1

if counter % 11 == 10:
    counter = 0
    index_counter = 0
    for digit in test_list2:
        counter = counter + digit * int(eeid[index_counter])
        index_counter += 1
    if counter % 11 == int(eeid[10]):
        print('Your id code is valid')
        print('Your national ID code is: ' + str(int_eeid))
        print('Your date of birth: ' + bth_day + '.' + bth_month + '.' + century  + bth_year)
        print('You are ' + gender)
    else:
        print('Your id code is not valid')
else:
    if counter % 11 == int(eeid[10]):
        print('Your id code is valid')
        print('Your national ID code is: ' + str(int_eeid))
        print('Your date of birth: ' + bth_day + '.' + bth_month + '.' + century + bth_year)
        print('You are ' + gender)
    else:
        print('Your id code is not valid')