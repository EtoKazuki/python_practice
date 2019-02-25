import readchar as rc

while 1:
    kb = rc.readchar()
    print(kb)
    if kb == 'q':
        print(kb, end='', flush=True)
        break
