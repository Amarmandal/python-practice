# # Raw stream input
# raw_log = "SSSWWESSS"

# # Expected output from generator consumption
# list(compress_stream(raw_log))
# # Output: [('S', 3), ('W', 2), ('E', 1), ('S', 3)]

def compress_stream(raw_log): 
    stream = iter(raw_log)
    run_length = 1

    try: 
        current_char = next(stream)
        run_length = 1
    except StopIteration: 
        return 
    
    for char in stream: 
        if current_char != char: 
            yield (current_char, run_length)
            run_length = 1
            current_char = char
        else: 
            run_length += 1

    yield (current_char, run_length)



def main(): 
    raw_log = "SSSWW"
    
    result = (val for val in compress_stream(raw_log))

    print(list(result))


if __name__ == "__main__": 
    main()