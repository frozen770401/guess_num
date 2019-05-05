import random

start_num = input('請輸入亂數起始值: ')
end_num = input('請輸入亂數終結值: ')
start_num = int(start_num)
end_num = int(end_num)

r = random.randint(start_num, end_num)
guess = 0
count = 0
while guess != r:
	guess = input('請猜數字: ')
	guess = int(guess)
	count += 1
	print('第', count, '次猜')
	if guess == r:
		print('猜對了!')
	else:
		print('猜錯囉~')
		if r < guess:
			print('猜小一點')
		else:
			print('猜大一點')