a=()
n=int(input("Enter the number of elements"))
for i in range(0,n):
	no=int(input())
	a=a+(no,)
print(a)
for i in range(0,n//2):
	if a[i]!=a[n-i-1]:
		print("Not symmetric")
		break
else:
	print("symmetric")




