a=set()
n=int(input("Enter the number of elements : "))
print("Enter the elements")
for i in range(0,n):
	no=int(input())
	a.add(no)
print(a)
s=0
for x in a:
	if x%2==0:
		s+=x
print("Sum is ",s)