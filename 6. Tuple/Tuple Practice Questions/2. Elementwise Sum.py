def tuple_elementwise_sum(tuple1, tuple2):
    if len(tuple1) != len(tuple2):
        raise ValueError("Input tuples must have the same length.")
 
    result = tuple(a + b for a, b in zip(tuple1, tuple2))
    print(result)

tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6)
tuple_elementwise_sum(tuple1, tuple2)