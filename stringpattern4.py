word=input("Enter a string : ")
k=len(word)
k=(k+1)*-1
for i in range(k,-1):
	print(word[-1:i:-1])



