a="Hello"
b='good'
print(type(a))
print(type(b))

l1=len(a)
for i in range(0,l1):
	print(a[i],end="->")
print()
for i in b:
	print(i,end="-")
