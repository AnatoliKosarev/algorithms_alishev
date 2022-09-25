def fib_recursive(index, result_list):
    if result_list[index] != -1:
        return result_list[index]

    if index <= 1:
        return index

    result = fib_recursive(index-1, result_list) + fib_recursive(index-2, result_list)
    result_list[index] = result

    return result


index_input = 4
result_list = [-1 for i in range(index_input+1)]
print(fib_recursive(index_input, result_list))
