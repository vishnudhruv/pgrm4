a=()
n=int(input("Enter the number of elements"))
for i in range(0,n):
	no=int(input())
	a=a+(no,)
print(a)
b=list(a)
no=int(input("Enter the element :"))
index=int(input("Enter the index "))
b.append(0)							
for i in range(n,index,-1):
	b[i]=b[i-1]
b[index]=no
a=tuple(b)
print(a)

