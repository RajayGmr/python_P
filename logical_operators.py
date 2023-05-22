temp = int(input("What is the temperature outside?:"))

if temp>=0 and temp<=15:
    print("The weather is cool")
    print("Stay warm")
elif temp>15 and temp<25:
    print("The weather is good today")
    print("Go outside and see the world")
elif temp>25 and temp<40:
    print("The weather is hot today.")
    print("Stay Hydrate")
elif temp<0 or temp>40:
    print("The weathe is bad today")
    print("Better stay at home")