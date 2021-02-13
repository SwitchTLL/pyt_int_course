# counter = 0
# while counter <1000001:  # while False: - exits without result / while True - forever loop
#     print("I can't stop!!! " + str(counter) + ' times')
#     counter += 1



condition = True
counter = 3  # Try's counter for 3 times

while condition and counter > 0:
    user_input = input('Please enter your id code:')
    if len(user_input) != 11:  # Length of user input string
        print('Please try again')
        counter -= 1  # counter of false try +1
        if counter != 0:
            print("please try again")
        else:
            print("Ran out of tries")
    else:
        print(user_input)
        condition = False  # Exit condition

