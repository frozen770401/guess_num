import random

r = random.randint(1, 100)
guess = 0
while guess != r:
	guess = input('請猜數字: ')
	guess = int(guess)
	if guess == r:
		print('猜對了!')
	else:
		print('猜錯囉~')
		if r < guess:
			print('猜小一點')
		else:
			print('猜大一點')