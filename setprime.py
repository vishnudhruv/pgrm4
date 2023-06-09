a=set()
n=int(input("Enter the number of elements : "))
print("Enter the elements")
for i in range(0,n):
	no=int(input())
	a.add(no)
print("Prime numbers : ")
for x in a:
	if x==1:
		continue
	for j in range(2,x):
		if x%j==0:
			break
	else:
			print(x)