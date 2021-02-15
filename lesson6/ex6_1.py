#id_code = input("Please enter your ID code: ")

#1, 2, 3, 4, 5, 6, 7, 8, 9, 1,
#3, 4, 5, 6, 7, 8, 9, 1, 2, 3,

#result = 1 * int(id_code[0] + 2 * int(id_code[1]))

# or method
id_code = input('Please enter you EE ID code: ')

def check_id(id_code)
    def count_check_number(id_code, chk_list):
        result = 0
        counter = 0
        for num in chk_list:
            result = result + num * int(id_code[counter])
            counter += 1
        return result % 11

    id_code = input("Please enter your ID code: ")
    chk1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 1,]
    chk2 = [3, 4, 5, 6, 7, 8, 9, 1, 2, 3,]

print(count_check_number(id_code, chk2) % 11)

if int(id_code[10]) == count_check_number(id_code, chk1):
    print('ID code is valid')
elif count_check_number(id_code, chk1) == 10:
        if int(id_code[10] == count_check_number(id_code, chk2)):
        elif result % 11 == 10 or result % 11 == 0) # and int(id_code[10] == 0)
        if int(id_code[10] == 0):
            print('ID code is valid')
        else:
            (print('ID code is not valid'))
        else:
            (print('ID code is not valid'))

        print(count_check_number(id_code))

check_id()