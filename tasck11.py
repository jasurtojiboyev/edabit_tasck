name = "outstanding"
m = len(name)
for x in range(1, m+1):
    n = name[0]
    b = name[1]
v = n+b
del n, b
print(f"{v}... {v}... {name}?")
