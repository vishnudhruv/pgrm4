name=input("Enter the name : ")
l=len(name)
for i in range(0,l-1):
	if name[i]==" ":
		continue
	elif name[i+1]==" ":
		print(name[i],end="")
	else:
		print("<",name[i],">",end="")
print(name[l-1])

