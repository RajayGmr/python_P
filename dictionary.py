capitals = {
    'USA':"Washington DC",
    'India':"New Dehli",
    'Thailand':"Bangkok",
    'Myanmar':"Rangoon",
    'China':"Beijing"
}
capitals.update({"Germany":"Berlin"})
capitals.update({'Myanmar':'Nay Pyi Taw'})
print(capitals['Germany'])
print(capitals.get('Norway'))
print(capitals.keys())
print(capitals.values())
print(capitals.items())
capitals.pop('China')

for key,value in capitals.items():
    print(key,value)