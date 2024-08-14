def whereIsWaldo(arr):
    elements = []
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            elements.append((arr[i][j], i + 1, j + 1))
    
    counts = {}
    for element in elements:
        value = element[0]
        if value in counts:
            counts[value].append(element[1:])
        else:
            counts[value] = [element[1:]]
    
    for key, value in counts.items():
        if len(value) == 1:
            return value[0]

# Test cases
print(whereIsWaldo([
  ["A", "A", "A"],
  ["A", "A", "A"],
  ["A", "B", "A"]
]))  # Output: [3, 2]

print(whereIsWaldo([
  ["c", "c", "c", "c"],
  ["c", "c", "c", "d"]
]))  # Output: [2, 4]

print(whereIsWaldo([
  ["O", "O", "O", "O"],
  ["O", "O", "O", "O"],
  ["O", "O", "O", "O"],
  ["O", "O", "O", "O"],
  ["P", "O", "O", "O"],
  ["O", "O", "O", "O"]
]))  # Output: [5, 1]