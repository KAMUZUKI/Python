while True:
    try:
        num = int(input('请输入一个数字'))
    except ValueError :
        print('请输入一个数字')
        continue
    if num.isdigit():
        if (num %2)==0:
             print('这是一个偶数')
        else:
             print(('这是一个奇数'))
    else:
        break