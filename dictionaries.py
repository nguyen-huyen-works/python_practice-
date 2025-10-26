# here is a list of scores 
scores = [90, 85, 78]
print(sum(scores)/len(scores))  # average

# here is a dictionary with key value
student = {"name": "Huyen", "major": "EE"}
print(student["name"])

# hi

# Unpacking is a way of not indexing directly 
student = ("Huyen", "EE", 19)
name, major, age = student
print(name, major, age)


# List lookup only cares about order and position
students = ["Huyen", "Linh", "Anh"]
print("Anh" in students)  # checks each element one by one → O(n)

# Dict lookup cares about the value (key value pairs) 
grades = {"Huyen": 90, "Linh": 85, "Anh": 78}
print("Anh" in grades)    # checks key instantly → O(1)




# found = False
# for name in students:
#     if name == "Anh":
#         found = True
#         break

# print(found)


# if you want to print a value inside a dictionary from each key 
print(78 in grades.values())  # ✅ True

# for a dictionary, name is not the index, it's actually the key. hence the difference between ditctionary and list. 
# use .items to pair with key and value from the dictionary 
for name, score in grades.items(): 
    if score == 78: 
        print(name) 