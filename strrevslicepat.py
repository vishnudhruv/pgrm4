word=input("Enter a string")
l=len(word)
for i in range(1,l+1):
	print(word[(-1):-1*(i+1):-1])


