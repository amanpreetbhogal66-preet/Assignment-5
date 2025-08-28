students = {
    "Aman" : 89,
    "Raman" : 80,
    "Deep" :88,
    "Jass" :85
}
name = input("Enter the student's name: ")
if name in students:
    print(f"{name}'s marks: {students[name]}")
else:
    print(f"student'{name}' not found.")