def advanced_sort(lst):
    item_dict = {}
    
    for item in lst:
        if item not in item_dict:
            item_dict[item] = [item]
        else:
            item_dict[item].append(item)
    
    return list(item_dict.values())

print(advanced_sort([2, 1, 2, 1]))
print(advanced_sort([5, 4, 5, 5, 4, 3]))
print(advanced_sort(["b", "a", "b", "a", "c"]))