def count_vowels(input_string):
    vowels = 'aeiouAEIOU'
    count = 0
    for char in input_string:
        if char in vowels:
            count += 1
    return count

print(count_vowels("Celebration"));
print(count_vowels("Palm"));
print(count_vowels("Prediction"));