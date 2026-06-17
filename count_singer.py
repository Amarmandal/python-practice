N = int(input())
songs = input()

counter = {}

def favorite_singer(playlist): 
    data = playlist.split()
    
    for val in data: 
        counter[val] = counter.get(val, 0) + 1


    max_freq = max(counter.values())
    
    total_count = sum(1 for val in counter.values() if val == max_freq)

    return total_count



if __name__ == "__main__": 
    print(favorite_singer(songs))

