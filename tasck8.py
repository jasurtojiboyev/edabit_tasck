massiv = [1, 2, 2, "a", "b"]
m = []
for x in massiv:
    if type(x) == int:
        m.append(x)

    else:
        del x

print(m)