word=input("Enter a string : ")
k=len(word)
k=k*-1
for i in range(-1,k-1,-1):
	print(word[i::-1])