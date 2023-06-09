word=input("Enter a string")
l=len(word)
for i in range(l-1,-1,-1):
	for j in range(l-1,i-1,-1):
		print(word[j],end=" ")
	print()



