num1 = "abcde"
num2 = "abcde"
i = 0
resulte = 0
while i < len(num1):
    while i < len(num2):
        x = num1[i]
        y = num2[i]
        if y != x:
            resulte += 1
        i += 1

print(resulte)

