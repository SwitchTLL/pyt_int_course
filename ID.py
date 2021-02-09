import sys,time

# def sprint(str):
#    for c in str + '\n':
#      sys.stdout.write(c)
#      sys.stdout.flush()
#      time.sleep(0.05)

print("Please enter you ID code:")
isikukood = input(int())
birthdate = isikukood[1:8]
#isikukood: str = "12345678909"

if int(len(isikukood)) == 11:  #ID length checker
    print("ID length check:\nPASSED")
else:
    print("ID length check:\nFAILED")

# ID sex checker
num_id = list(isikukood)
print(num_id)
sex = int(num_id[0])
print(sex)
num_id2 = list(isikukood)
print(num_id2)

print("ID code gender check:")
if (sex % 2 == 0):
    print("Gender check:\nMALE")
else:
    print("Gender check:\nFEMALE"

#    if sex == "2" or "4" or "6" or "8" or "0":
#        print("Sex check PASSED = FEMALE")
