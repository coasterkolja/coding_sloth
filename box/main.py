def makeBox(n):
    if n == 1:
        return ["#"]
    
    top_bottom_row = "#" * n
    middle_row = "#" + " " * (n - 2) + "#"
    
    box = [top_bottom_row] + [middle_row] * (n - 2) + [top_bottom_row]
    
    return box

print(makeBox(5))
print(makeBox(3))
print(makeBox(2))
print(makeBox(1))