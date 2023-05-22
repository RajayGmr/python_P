food = ["pizza","Coke","KFC","Subway", "hotdog"]
food[2]="Korean Chicken"
print(food[2])
food.append("ice cream")
food.remove("Subway")
food.pop()
food.insert(0,"Orange Juice")
food.sort()
#food.clear()
for i in food:
    print(i, end=", ")