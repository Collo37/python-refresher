# lists (arrays)

names = ["Collins", "Derrick", "Oduor", "Collo Sama", "Dev Collins"]
# list methods
names.append("Collosso")
print("Appended Collosso", names)

copy_of_names = names.copy()
print(names, copy_of_names)

print("Number of occurences of Collins", names.count("Collins"))

names.extend(["Collo", "Programmer"])
print("Extended list", names)

print("Index of Collo", names.index("Collo"))

names.insert(0, "Otaku")
print("insert", names)

names.remove("Programmer")
print("Removed Programmer", names)

names.pop()
print("Removed item at the last index", names)

names.reverse()
print("Reversed names", names)

names.sort()
print("Sorted names", names)

names.clear()
print("Cleared the list of names", names)

print("Copy of names", copy_of_names)