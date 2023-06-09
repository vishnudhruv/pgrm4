a=()
n=int(input("Enter the number of elements"))
for i in range(0,n):
	no=int(input())
	a=a+(no,)
print(a)
key=int(input("Enter the element to be searched : "))
count=0
for i in range(0,n):
	if a[i]==key:
		count+=1
print(key," occured ",count," times")