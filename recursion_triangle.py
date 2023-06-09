def backwardsby2(num):
	if num <= 0:
		#print('Zero!')
		return
	else:
		emojismiles = []
		for i in range(0, num):
			emojismiles += '❤️'
		print(' '.join(emojismiles))
		#print(emojismiles)
		backwardsby2(num - 1)
backwardsby2(9)