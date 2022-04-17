import random
number=random.randint(1,100)
guess=-1
start=1
end=100
while True:
    guess=int(input('請輸入{}~{}之間的數字來猜數：'.format(start,end)))
    if guess == number:
        print("猜中了，數字是：",number)
        break
    elif guess < number:
        print('{}~{}之間'.format(guess,end))
        start=guess
    else:
        print('{}~{}之間'.format(start,guess))
        end=guess
print('程式執行完畢')
