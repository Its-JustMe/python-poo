def menu (msg):
    print('*' * len(msg))
    print(msg)
    print('*' * len(msg))

def fatorial (num):
    if num <= 1:
       return 1
    else:
       return num * fatorial(num -= 1)