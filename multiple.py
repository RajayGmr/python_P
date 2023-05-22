#multiple assignment
name, age, attractive= "James", 34, True
print(name, age, attractive)

bob = james = john = 32
print(bob, james, john)

#useful method
name = "Jenny Careles"
print(len(name))
print(name.find("e"))
print(name.capitalize())
print(name.upper())
print(name.lower())
print(name.isdigit())
print(name.isalpha())
print(name.count("e"))
print(name.replace("e","a"))
print(name*3)

#type Casting
x = 1
y = 2.0
z = "3"
print(x, y, z)
print(int(y))
print(float(z))
sum = x+y+float(z)
print("The sum is:" +str(sum))