def sum_digit(num):
	if num==0:
		return 0
	s=num%10+sum_digit(num//10)
	return s
n=int(input("Enter a number : "))
sum=sum_digit(n)
print("Sum of digits : ",sum)
