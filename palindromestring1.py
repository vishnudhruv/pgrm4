word=input("Enter a word : ")
k=len(word)
rev=""
for i in range(0,k):
	rev=rev+word[k-i-1]
if word==rev:
	print("Palindrome")
else:
	print("not a Palindrome")