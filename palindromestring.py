word=input("Enter a string : ")
k=len(word)
for i in range(0,k//2):
	if word[i]!=word[k-i-1]:
		print("not a Palindrome")
		break
else:
	print("palindrome")







