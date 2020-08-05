import os.path

dic = {}

if not os.path.isfile('mydictionary.txt'):
    fo = open('mydictionary.txt','w')
    print('new file')
else:
    fo = open('mydictionary.txt','r')
    print('old file')

for row in fo.readlines():
    data = row.split(':')
    
    key = data [0]
    value = data[1]
    value = value.strip()
    
    dic[key]=value
print(dic)

fo.close()    
while True:
    print('1.set a vocab')
    print('2.print all the information')
    print('3.english to chinese')
    print('4.chinese to english')
    print('5.learning experience')
    print('6.leaving system')
    sel = input('enter ur option')
    if sel=='1':
        en = input('enter English:')
        ch = input('enter Chinese')
        dic[en]=ch
        
        fo = open('mydictionary.txt','w')
        for k,v in dic.items():
            fo.write(k)
            fo.write(':')
            fo.write(v)
            fo.write('/n')
        fo.closed()
    elif sel=='2':
        for k,v in dic.items():
            print(k,':',v)
    elif sel=='3':
        search = input('search english')
        print(dic[search])
    elif sel=='4':
        search1 = input('search chinese')
        for k,v in dic.items():
            if search1 == v:
                print(k)
    elif sel=='5':
        score=0
        for k,v in dic.items():
            print(v,':')
            ans = input('put ur answer here')
            if ans==k:
                print('correct')
                score = score + 1
            print('ur score:',score)
        
    
    
    elif sel=='6':
        break