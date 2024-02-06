def remove_duplicates(lst):
    unique = []
    seen = set()
    for item in lst:
        if item not in seen:
            unique.append(item)
            seen.add(item)
    print(unique)        

lst = [1, 1, 2, 2, 3, 4, 5]
remove_duplicates(lst)