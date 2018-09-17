x={"a","b","c"}
print(x)

x.add("d")
print(x)

# x.clear() //clears all the set
# print(x)  //prints set() ,doesn't throw an error

new=x.copy() #copy of the old set
print(new)

y={"c","f","g"}
z=x.difference(y) #prints {'d','a','b'} which r not common in x&y
print(z)

y={"c","f","g"}
z=x.difference_update(y) #prints {'d','a','b'} which r not common in x&y
print(z)