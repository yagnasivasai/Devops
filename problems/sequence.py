name ="yegnasivasai"
list=[1,2,3,4,5,6,7,8,9,10]
tuple=(1,2,3,4,5,6,7,8,9,10)

print(len(name))
print(list[0])
print(list[0:2])
print(list[:5])
print(name.count('a'))
#print(name.index('5'))
print(list.index(5))

result = [x**2 for x in [1,2,5,9]]
print(result)

list = [7,8,9]
for x in list:
    print(x**2)