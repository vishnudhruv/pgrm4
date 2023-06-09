def power(n,p):
	if p==0:
		return 1
	x=n*power(n,p-1)
	return x
n=int(input("Enter the number : "))
p=int(input("Enter the power : "))
print(power(n,p))