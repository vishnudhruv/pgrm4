s1=input("Enter a string : ")
s2=input("Enter another string : ")
l1=len(s1)
l2=len(s2)
for i in range(0,l1-l2+1):
	s3=s1[i:i+l2]
	if s3==s2:
		print(s2," present in ",i,"index")
		break
	
else:
	print(s2," not present")

S1=Trivandrum   l1=10
   0123456789
s2=drum		  l2=4
   0123