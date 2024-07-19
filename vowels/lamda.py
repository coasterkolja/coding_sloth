count_vowels = lambda s: sum(1 for char in s if char in 'aeiouAEIOU')

print(count_vowels("Celebration"))
print(count_vowels("Palm"));
print(count_vowels("Prediction"));