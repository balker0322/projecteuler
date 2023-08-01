from collections import deque


MAX_NUMBER = 28123 + 100


def main():

    num_list = [i+1 for i in range(MAX_NUMBER)]
    divisors = {n:[] for n in num_list}

    num_queue = deque(list(num_list))

    while num_queue:
        div = num_queue.popleft()
        running_sum = div
        while True:
            if div < running_sum:
                divisors[running_sum].append(div)
            running_sum += div
            if running_sum > MAX_NUMBER:
                break
        
    abundant_numbers = []

    for num, div_list in divisors.items():
        if sum(div_list) > num:
            abundant_numbers.append(num)

    sum_list = set([])
    for i in range(len(abundant_numbers)):
        for j in range(i, len(abundant_numbers)):
            num = abundant_numbers[i] + abundant_numbers[j]
            if num > MAX_NUMBER:
                break
            sum_list.add(num)
    
    num_queue = deque(list(num_list))
    for num in sum_list:
        if num in num_queue:
            num_queue.remove(num)

    result = sum(num_queue)

    print(result)
    

if __name__=='__main__':
    main()