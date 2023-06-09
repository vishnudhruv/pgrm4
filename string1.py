word=input("Enter your name : ")
cnt=0
for a in word:
	if a in ['a','e','i','o','u','A','E','I','O','U']:
		cnt=cnt+1
print(cnt)