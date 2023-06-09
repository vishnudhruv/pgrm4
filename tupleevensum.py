a=()
n=int(input("Enter the number of elements"))
for i in range(0,n):
	no=int(input())
	a=a+(no,)
print(a)
s=0
for i in range(0,n):
	if a[i]%2==0:
		s+=a[i]
print("Sum is ",s)

