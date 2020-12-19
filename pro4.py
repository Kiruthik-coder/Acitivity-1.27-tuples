clg_list = []
clg_tuple = ()  # empty tuple
print("Enter Name of ten Clg :")
i = 1
while i <= 10:
    n = input("Name {} :".format(i))
    if n not in clg_list:
        clg_list.append(n)
    else:
        print("You have already entered this name !")
        continue
    clg_tuple = tuple(clg_list)
    print(clg_tuple)
    i += 1
