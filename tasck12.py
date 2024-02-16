a = input("Enter name: ")
person = {
    "Darth Vader": "father",
    "Leia": "sister",
    "Han": "brother in law",
    "R2D2": "droid"
}
for people in person.keys():
    if a == people:
        print(f"Luke I'm your {person[people]}")
        break
else:
    print("Nope")