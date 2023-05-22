import time
name= ""
while len(name) == 0:
    name=input("Enter your name: ")

print("Hello "+ name)

for i in range(10):
    print("Range is:"+ str(i+1))

for i in range(50,100+1,2):
    print("Range 50 - 100 is:"+ str(i))

for i in "James Smith":
    print(i)

for seconds in range(10,0,-1):
    print(seconds)
    time.sleep(1)
print("Happy New year!"+ name)