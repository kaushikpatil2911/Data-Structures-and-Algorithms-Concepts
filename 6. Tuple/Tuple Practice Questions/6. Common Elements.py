def common_elements(tuple1, tuple2):
    print(tuple(set(tuple1) & set(tuple2)))

tuple1 = (1, 2, 3, 4, 5)
tuple2 = (4, 5, 6, 7, 8)
common_elements(tuple1, tuple2)    