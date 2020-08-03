import random
a = 1
b = 100
num = random.randint(a,b)
while True:
    print('the number is inbetweem%d-%d'%(a,b))
    ans = int(input('enter a number:'))
    if ans<a or ans>b:
        print('the number is invalid')
    elif ans>num:
        b = ans
    elif ans<num:
        a = ans
    elif ans==num:
        print('add point')
        break
