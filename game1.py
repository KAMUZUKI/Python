import random
print('*'*30)
print('欢迎来小游戏！！')
print('*'*30)
username1 = 'MU'
password1 = '123456'
username = input('请输入用户名：')
password = input('请输入密码：')
money = 0
while username1 == username and password == password1:
	answer = input('是否进入游戏(y or n):')
	if answer == 'y' and money >= 2:
		money -= 2
		t1 = random.randint(1, 6)
		t2 = random.randint(1, 6)
		guess = input('请输入大或小:')
		if (t1+t2) > 6 and guess == '大' or (t1+t2) <= 6 and guess == '小':
			money += 3
			print('猜对了，金币加3！当前金币为{}'.format(money))
		else:

			print('猜错了，金币减2,当前金币为{}'.format(money))
	else:
		if answer == 'n' or (answer == 'n' and money < 2):
			print('退出游戏，请稍后！')
		else:
			print('金币不足，请充值！')
			f = int(input('请输入充值金额：'))
			money += f
else:
	print('用户名或密码错误，请重新输入：')