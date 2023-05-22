name = "James Smith"

first_name=name[0:6]
last_name=name[6:12]
funky_name=name[0:12:3]
reversed_name=name[::-1]

print(first_name)
print(last_name)
print(funky_name)
print(reversed_name)

website = "https://google.com"
website2= "https://facebook.com"
slice = slice(8,-4)
print(website[slice])
print(website2[slice])