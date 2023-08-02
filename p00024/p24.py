

def factorial(n):

    if n <= 1:
        return 1
    
    return n*factorial(n-1)


def get_nth_lex_perm(
        nth:int,
        digits:str):
    
    digits_cnt = len(digits)

    if digits_cnt == 1:
        return digits
    
    q, r = divmod(nth-1, factorial(digits_cnt-1))
    next_digit = digits[q]

    return next_digit + get_nth_lex_perm(r+1, digits.replace(next_digit, ''))


def main():
    nth = 1000000
    digits = "0123456789"
    result = get_nth_lex_perm(nth, digits)
    print(result)


if __name__=='__main__':
    main()