condition = True  # Цикл ожидания комманды exit()/quit()
while condition:
    user_choice = input('Please choose:\n1. Check ID\n0. Exit\n--> ')

    # If statement for user choose option
    if user_choice == '1':

        condition2 = True
        while condition2:
            try:
                user_id = input('Please enter your Estonian national ID: ')
                user_id = str(int(user_id))
                if len(user_id) != 11:  # ID Length checker
                    if len(user_id) > 11:
                        print('Code you entered is is longer than 11 digits')
                    elif len(user_id) < 11:
                        print('Code you entered is shorter than 11 digits')
                    raise UserWarning
            except ValueError:
                print('Entered value is not numerical')
                print('Please try again!')
            except:
                print('ERROR')
            else:
                gender_id = user_id[0]
                birth_year = user_id[1:3]
                birth_month = user_id[3:5]
                birth_day = user_id[5:7]
                birth_region = int(user_id[7:10])
                checksum = user_id[10]
                # Gender check
                if int(gender_id) % 2 == 0:
                    gender = 'Female'
                else:
                    gender = 'Male'
                # Century check
                if gender_id == '1' or gender_id == '2':
                    birth_cent = '18'
                elif gender_id == '3' or gender_id == '4':
                    birth_cent = '19'
                elif gender_id == '5' or gender_id == "6":
                    birth_cent = '20'
                elif gender_id == '7' or gender_id == '8':
                    birth_cent = '21'
                elif gender_id == '9' or gender_id == '0':
                    birth_cent = '22'

        # Region control
                if birth_region in range(1,11):
                    birth_region = 'Kuressaare haigla'
                elif birth_region in range(11, 20):
                    birth_region = "Tartu Ülikooli Naistekliinikum"
                elif birth_region in range(20, 151):
                    birth_region = 'Ida-Tallinna keskhaigla, Pelgulinna sünnitusmaja (Tallinn)'
                elif birth_region in range(150, 159):
                    birth_region = 'Keila haigla'
                elif birth_region in range(160, 219):
                    birth_region = 'Rapla haigla, Loksa haigla, Hiiumaa haigla (Kärdla)'
                elif birth_region in range(220, 269):
                    birth_region = 'Ida-Viru keskhaigla (Kohtla-Järve, endine Jõhvi)'
                elif birth_region in range(270, 369):
                    birth_region = 'Maarjamõisa kliinikum (Tartu), Jõgeva haigla'
                elif birth_region in range(370, 419):
                    birth_region = 'Narva haigla'
                elif birth_region in range(420, 469):
                    birth_region = 'Maarjamõisa kliinikum (Tartu), Jõgeva haigla'
                elif birth_region in range(470, 489):
                    birth_region = 'Haapsalu haigla'
                elif birth_region in range(490, 519):
                    birth_region = 'Järvamaa haigla (Paide)'
                elif birth_region in range(520, 569):
                    birth_region = 'Rakvere haigla, Tapa haigla'
                elif birth_region in range(570, 599):
                    birth_region = 'Valga haigla'
                elif birth_region in range(600, 649):
                    birth_region = 'Viljandi haigla'
                elif birth_region in range(650, 699):
                    birth_region = 'Lõuna-Eesti haigla (Võru), Põlva haigla '
                #else:
                    #birth_region = 'other region'

                print('Your national ID is: ' + user_id)
                print('You are ' + gender_id)
                print('Your date of birth is ' + birth_day + '.' + birth_month + '.' + birth_cent + birth_year)
                print('You were born in ' + birth_region)
                condition2 = False
    elif user_choice == '0':
        print('Good bye!')
        quit()
else:
        print('Choice is out of range')

# Homework = add ID code validation control. Check by ID - 38803160272
# https://et.wikipedia.org/wiki/Isikukood