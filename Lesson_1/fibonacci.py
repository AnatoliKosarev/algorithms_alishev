def fib_naive(index):
    if index <= 1:
        return index

    return fib_naive(index-1) + fib_naive(index-2)


print(fib_naive(3))
print(fib_naive(5))
print(fib_naive(10))


def fib_effective(index):
    fib_list = [0, 1]

    for i in range(2, index+1):
        fib_list.append(fib_list[i-1] + fib_list[i-2])

    return fib_list[index]


print(fib_effective(3))
print(fib_effective(5))
print(fib_effective(10))
print(fib_effective(101))
