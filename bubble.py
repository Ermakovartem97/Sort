def sort_fun(sort_list):
    iteration = 0
    for i in range(len(sort_list) - 1):
        if sort_list[i] > sort_list[i + 1]:
            sort_list[i], sort_list[i + 1] = sort_list[i + 1], sort_list[i]
    return [sort_list, iteration]
