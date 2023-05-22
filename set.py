utensils  = {"spoon","Knife","fork"}
dishes={"plate","cup","glass","bowl","spoon"}
#utensils.update(dishes)
dinner_table=utensils.union(dishes)
utensils.add("napkin")
utensils.remove("fork")
for i in utensils:
    print(i)

print("-----------------")

for i in dinner_table:
    print(i)

print(utensils.difference(dishes))
print(utensils.intersection(dishes))