""" 
Amicable numbers
Problem 21
 """

N = 10000

def get_proper_divisors(num):
    proper_divisors = []
    for i in range(num):
        if num%(i+1)==0:
            if i+1 in proper_divisors:
                break
            proper_divisors.append(i+1)
            proper_divisors.append(int(num/(i+1)))
    proper_divisors.remove(num)
    return proper_divisors

def get_amicable_numbers(num_range):
    num_list = set([x+1 for x in range(num_range)])
    amicable_numbers = []

    while len(num_list) > 1:
        current_num = list(num_list)[0]
        sum1 = sum(get_proper_divisors(current_num))
        while True:

            if sum1 == current_num:
                num_list.remove(current_num)
                break

            if sum1 not in num_list:
                num_list.remove(current_num)
                break

            sum2 = sum(get_proper_divisors(sum1))

            if current_num == sum2:
                amicable_numbers.append(int(current_num))
                amicable_numbers.append(int(sum1))
                num_list.remove(current_num)
                num_list.remove(sum1)
                break
            
            num_list.remove(current_num)
            num_list.remove(sum1)

            if sum2 not in num_list:
                break

            current_num = sum2
            sum1 = sum(get_proper_divisors(current_num))


    return amicable_numbers

def main():
    x = get_amicable_numbers(N)
    x = sum(x)
    print(x)

if __name__=='__main__':
    main()