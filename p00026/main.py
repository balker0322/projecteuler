
def calc(d:int):
    mem = {}
    a = 1
    n = 1
    while True:
        if a in mem.keys():
            return n - mem[a]
        q = (10*a)%d
        if q == 0:
            return 0
        mem[a] = n
        a = q
        n += 1
    
def main():
    max_len = 0
    ans = 1
    for i in range(1, 1000):
        l = calc(i)
        if l > max_len:
            max_len = l
            ans = i
    print(ans)

if __name__=='__main__':
    main()
    