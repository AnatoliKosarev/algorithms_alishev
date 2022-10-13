def max_number_from_list(list):
    str_sorted_list = ''.join([str(el) for el in sorted(list, reverse=True)])
    # str_sorted_list = ''.join((map(lambda x: str(x), sorted(list, reverse=True))))
    result = int(str_sorted_list) if str_sorted_list.isdigit() else False
    return result


test_list = [3, 1, 7, 9, 9, 5]
print(max_number_from_list(test_list))
