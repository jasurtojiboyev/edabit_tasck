m = "ooxx"
resulte = 0
resulte2 = 0
n = [False]
for x in m:
    if x == "o":
        resulte += 1
    if x == "x":
        resulte2 += 1
    if resulte == resulte2:
        print(True)
if resulte2 < resulte or resulte2 > resulte:
    print(False)



