def sum_factorial(lst):
    sum = 0
    for n in lst:
        prod = 1
        for m in range(1, n+1):
            prod *= m
            print(prod)
        sum +=prod
        print(sum)

sum_factorial([5, 6])