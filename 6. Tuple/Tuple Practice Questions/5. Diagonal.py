def get_diagonal(tup):
    print(tuple(tup[i][i] for i in range(len(tup))))

tup = (
    (1, 2, 3),
    (4, 5, 6),
    (7, 8, 9)
)
get_diagonal(tup)
