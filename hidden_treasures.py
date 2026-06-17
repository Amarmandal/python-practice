n = int(input())
nums = list(map(int, input().split()))

def digit_sum(n): 
    total = 0 

    while n: 
        total += n % 10 
        n //= 10 
    
    return total


def solve (n, nums):
    sum_of_digits = []
    # Write your code here
    for i in range(n): 
        sum_of_digits.append(digit_sum(nums[i]))

    frequency_count = {}

    for val in sum_of_digits: 
        frequency_count[val] = frequency_count.get(val, 0) + 1

    pair_possible = sum(n * (n-1) // 2 for n in frequency_count.values() if n > 1)

    return pair_possible



out_ = solve(n, nums)
print (out_)


