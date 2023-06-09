lst=[]
n=int(input("Enter the number of elements : "))
print("Enter the elements")
for i in range(0,n):
	no=int(input())
	lst.append(no)
numbers=set(lst)
for x in numbers:
	print(x)