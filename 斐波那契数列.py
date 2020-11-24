
# 第一和第二项
n1 = 0
n2 = 1
a = 1
count = 2
nterms = int(input("你需要几项？"))
# 判断输入的值是否合法
if nterms <= 0:
    print("请输入一个正整数。")
elif nterms == 1:
    print("斐波那契数列：")
    print(n1)
else:
    print("斐波那契数列：")
    print('这是起始项；0' + '\n' +  '这是第1项：1')
    while count < nterms:
        nth = n1 + n2
        a = a+1
        print('这是第%d项:'%a, nth, end=" ,\n ")
        # 更新值
        n1 = n2
        n2 = nth
        count += 1
