# -*- coding: UTF-8 -*-
#!/usr/bin/python2.7

def hello():
    print('''hello
    
    "ooo" 'ppp'
    world''')

    print(' "hhh"')
    title="my name:"
    name="alun"

    print(title+name)
    age=30
    temp=2
    print(age+temp)
    print(str(age) + name)
    print('{} {} {}'.format('my name','is',name))
    # 32alun

    list=["a",2,"b","c"]
    print(list[0])
    print(list[1])

    a="adafdsfdfdfdfdfdfewrwerwerwrwerwerwerwerwerewr"

    print('------------')
    for v in list:
        print(v)


    sum = 0
    counter = 1
    n = 100
    while (counter <= n):
        sum = sum + counter
        counter += 1
        if counter==80 :
            print(counter)


def  n9x9():
    # 九九乘法表
    for i in range(1, 10): # 1,2,3,4,5,6,7,8,9
        for j in range(1, i + 1):
            print('{}x{}={}\t'.format(j, i, i * j), end='')
        print()



hello()
n9x9()