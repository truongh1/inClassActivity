def divisor(num):
    for x in range(1, num -1):
        if (num % x ==0):
            print(x)

x = 36
divisor(x)