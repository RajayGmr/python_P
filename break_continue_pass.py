while True:
    name = input("Enter your name: ")
    if name != "":
        break
    print("Break")

phone_number="123-456_7890"
for i in phone_number:
    if i == "-" or i == "_":
        continue
    print(i, end=" ")
    print("Continue")

for i in range(1,15):
    if i == 13:
        pass
    else:
        print(i, end=" ")
        print("pass 13")