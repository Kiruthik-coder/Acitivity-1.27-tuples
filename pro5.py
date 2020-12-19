num_tup = ()
num_lst = []
for i in range(101, 200):
    if i % 2 == 0:
        num_lst.append(i)
        num_tup = tuple(num_lst)
        print(num_tup)
