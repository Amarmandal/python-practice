import sys 

N  = int(sys.stdin.readline().strip())
black_char = "#"
white_char = "."


def solve(): 
    final_shape = []

    for _ in range(N): 
        R, C = [int(val.strip()) for val in sys.stdin.readline().split()]

        counter = 0 
        row_max_border = 0 
        col_max_border = 0

        current_lines = []

        # Read all the lines first 
        for _ in range(R): 
            line = sys.stdin.readline().strip()
            current_lines.append(line)
        
        # Row Scan
        for line in current_lines: 
            for char in line: 
                if char == white_char: 
                    counter = 0
                else: 
                    counter += 1
                    row_max_border = max(row_max_border, counter)
            counter = 0

        counter = 0 

        # Col Scan 
        for j in range(C): 
            for line in current_lines: 
                char = line[j]

                if char == white_char: 
                    counter = 0
                else: 
                    counter += 1
                    col_max_border = max(col_max_border, counter)
            counter = 0

        
        final_shape.append(max(row_max_border, col_max_border)) 

    return final_shape

    


if __name__ == "__main__": 
    for val in solve():
        print(val)


