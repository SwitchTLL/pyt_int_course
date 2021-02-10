# try, except, else, finally
#try:
#    print(1234 + 'abc')  # typical TypeError

  # Строку с ошибкой лучше проверять вне команды try: а в отдельном пустом файле
# user_id = input("Please enter your id:")
# try:
#     user_id = int(user_id)  # Проверка user_id на цифровое значенеи
# except:
#     print('ERROR')

user_id = input('Please enter your national ID:')
try:
    user_id = int(user_id)
    if len(user_id) != 11:
        raise UserWarning
except: TypeError
    print("ERROR")
except user:
    print("The code you entered in not numeric")
else:
    print(user_id)
finally:
    print('Program stopped working')