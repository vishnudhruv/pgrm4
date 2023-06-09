def sum(n):
	if n==1:
		return 1
	s=n+sum(n-1)
	return s
no=int(input("Enter the number : "))
s=sum(no)
print("Sum is : ",s)
