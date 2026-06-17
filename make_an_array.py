import sys 

T = int(sys.stdin.readline().strip())

def solve(test_case): 
    output = []

    for _ in range(test_case): 
        N = int(sys.stdin.readline().strip())
        A = [int(x) for x in sys.stdin.readline().strip().split()]

        if sum(A) % (N - 1) != 0: 
            output.append(-1)
            continue 

        max_a = max(A)
        number_steps = sum(A) // (N - 1)

        if max_a > number_steps: 
            output.append(-1)
            continue 

        output.append(number_steps)

    return output



if __name__ == "__main__": 
    for val in solve(T): 
        print(val)