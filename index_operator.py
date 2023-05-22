name = "james smith!"
first_name=name[0:5].upper()
last_name=name[6:].capitalize()
last_char=name[-1]
if(name[0].islower()):
    name=name.capitalize()
print(name)

print(first_name)
print(last_name)
print(last_char)