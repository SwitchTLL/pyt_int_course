user_set = input("Please enter 1st set of numbers:")
frequencies = collections.Counter(user_set)
repeated = {}

for key, value in frequencies.items():
    if value > 1:

        repeated[key] = value
print(repeated)