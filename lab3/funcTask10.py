def unique_list(lst):
    unique = []
    for i in lst:
        if i not in unique:
            unique.append(i)
    return unique

print(unique_list([1,2,2,3,4,4,5]))
