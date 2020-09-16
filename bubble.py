def sort_bubble(sort_list):
    iteration = 0
    j = 0
    end_list = len(sort_list) - 1
    for i in range(len(sort_list) - 1):
        while j < end_list:
            if sort_list[j] > sort_list[j + 1]:
                sort_list[j], sort_list[j + 1] = sort_list[j + 1], sort_list[j]
            iteration += 1
            end_list -= 1
            j += 1
    return [sort_list, iteration]
