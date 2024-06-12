def most_frequent(input_string):
    char_frequency = {}
    for char in input_string:
        if char.isalpha():
            char_frequency[char] = char_frequency.get(char, 0) + 1
    sorted_frequency = sorted(char_frequency.items(), key=lambda x: x[1], reverse=True)  
    for char, frequency in sorted_frequency:
        print(f"{char} = {frequency:02d}")

input_string = "Misssissippi"
most_frequent(input_string)
