def move(input_string):
    result = ""
    
    for char in input_string:
        next_char = chr(ord(char) + 1)
        result += next_char
    
    return result

print(move("hello"))
print(move("bye"))
print(move("welcome"))