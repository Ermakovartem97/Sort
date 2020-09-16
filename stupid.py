def sort_stupid(sort_list):
    iteration = 0
    for i in range(len(sort_list) - 1):
        for j in range(len(sort_list) - i - 1):
            iteration += 1
            if sort_list[j] > sort_list[j + 1]:
                sort_list[j], sort_list[j + 1] = sort_list[j + 1], sort_list[j]
    return [sort_list, iteration]