numbers={""}
n=int(input("Enter the number of elements : "))
print("Enter the elements")
for x in range(1,n+1):
	no=int(input())
	numbers.add(no)
for x in numbers:
	print(x)