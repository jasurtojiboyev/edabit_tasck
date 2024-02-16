string = "the aardvark"
simbol = "*"
vowels = "aouie"
result = ""
for item in string:
    if item in vowels:
            result = result + simbol
    else:
        result = result + item
print(result)