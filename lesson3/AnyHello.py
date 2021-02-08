string_sample = """Insert the price Python inside the placeholder, the price should be in fixed point, two-decimal format Python"""

if ("python" in string_sample) or ("Python" in string_sample) or ("the" in string_sample):  #and/or
    print(string_sample.count("Python" and "the"))
else:
    print("ERROR")