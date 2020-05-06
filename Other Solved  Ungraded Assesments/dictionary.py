'''inventory= {'apple':430512,'bananas':312,'oranges':525,'pears':217}
print(inventory)
del inventory['pears']
print(inventory)
inventory['pears']=0
inventory['bananas']=inventory['bananas']+100
print(inventory)
print(len(inventory))'''

'''#DICTIONARY OPERATIONS
inventory= {'apple':430512,'bananas':312,'oranges':525,'pears':217}
print(inventory)
inventory['bananas']=inventory['bananas']+100
print(inventory)'''

#DICTIONAY METHODS
'''#1 inventory= {'apple':430512,'bananas':312,'oranges':525,'pears':217}
print(inventory)
for key in inventory.keys():
	print(key,"has the value",inventory[key])

list_of_keys=list(inventory.keys())
print(list_of_keys)'''

'''
inventory= {'apple':430512,'bananas':312,'oranges':525,'pears':217}
print(inventory)
print(list(inventory.values()))
print(list(inventory.items()))

if 'apple' in inventory:
	print("apple is in inventory")
	print('apple' in inventory)


print(inventory.get("apple"))
print(inventory.get("not in inventory")) # it print none
print(inventory.get("not in inventory",0)) #it will print 0

'''
#aliasing and copying

