word=input("Enter a string")
newstring=""
l=len(word)
i=0
j=l-1
while i<l//2:
	newstring+=word[i]
	newstring+=word[j]
	i+=1
	j-=1
if l%2!=0:
	newstring+=word[i]
print(newstring)
