#list1 = [1,2,3,4]
#list2=[ list1[0] , list1[-1] ]
#print(list2)


# = [1,1,2,3,5,8,13,21,34,55,89]
#istb = a[:5]
#print(istb)



a = [1,1,2,3,5,8,13,21,34,55,89]
b = [1,2,3,4,5,6,7,8,9,10,11,12,13]
c = []

for value1 in a:
	for value2 in b:
		if value1 == value2:
			c.append(value2)
print(c)