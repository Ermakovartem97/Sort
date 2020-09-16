def sort_cocktaill(sort_list):
    iteration = 0
    start_list = 1
    i = 0
    end_list = len(sort_list) - 1
    while i != len(sort_list) // 2:
        if i == start_list:
            while i < end_list:
                if sort_list[i] > sort_list[i + 1]:
                    sort_list[i], sort_list[i + 1] = sort_list[i + 1], sort_list[i]
                i += 1
            end_list = i
            while i > start_list:
                if sort_list[i] < sort_list[i - 1]:
                    sort_list[i], sort_list[i - 1] = sort_list[i - 1], sort_list[i]
                i -= 1
            start_list = i
            iteration += 1
    return [sort_list, iteration]
