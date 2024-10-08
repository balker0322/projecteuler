
def fib(n):
    a = 1
    b = 0
    while n > 1:
        a, b = a+b, a
        n = n - 1
    return a

def main():
    n = 1
    while True:
        ans = fib(n)
        l = len(str(ans))
        if l >= 1000:
            print(n)
            exit()
        n += 1


if __name__=='__main__':
    main()
    