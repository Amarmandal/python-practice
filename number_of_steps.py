import sys 

n = int(sys.stdin.readline())
a = [int(val) for val in sys.stdin.readline().strip().split()]
b = [int(val) for val in sys.stdin.readline().strip().split()]


def is_all_equal(arr): 
    return all(x == arr[0] for x in arr)

def make_array_equal(arr_a, arr_b): 
    current_target = min(arr_a) # target
    accumulated_steps = 0 

    while True: 
        if current_target < 0: 
            return -1 
        
        if is_all_equal(arr_a):
            return accumulated_steps
        
        for i in range(n):
            if arr_a[i] > current_target: 
                if arr_b[i] == 0:
                    return -1

                # reduce the element
                n_step = (arr_a[i] - current_target + arr_b[i] - 1) // arr_b[i]
                arr_a[i] = arr_a[i] - (n_step * arr_b[i])
                accumulated_steps += n_step

                if arr_a[i] < current_target: 
                    current_target = arr_a[i]
    


if __name__ == "__main__": 
    print(make_array_equal(a, b))