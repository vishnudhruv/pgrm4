word=input("Enter a string : ")
l=len(word)
print("Length of the string is ",l)
print("Type of word is ",type(word))
for x in word:
	print(x)
for i in range(0,l):
	print(word[i])