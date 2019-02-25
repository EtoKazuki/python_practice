def double():
    num = int(input("10進数>"))
    first = num
    b128 = num // 2**7
    num = num%2**7
    b64 = num // 2**6
    num = num%2**6
    b32 = num // 2**5
    num = num%2**5
    b16 = num // 2**4
    num = num%2**4
    b8 = num // 2**3
    num = num%2**3
    b4 = num // 2**2
    num = num%2**2
    b2 = num // 2
    num = num%2
    binary = str(b128)+str(b64)+str(b32)+str(b16)+str(b8)+str(b4)+str(b2)+str(num)
    print(first, '=' ,binary, sep = ' ')
