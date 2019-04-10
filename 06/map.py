def my_map(function, list):
    new_list = []
    for item in list:
        new_list.append(function(item))
    return new_list


def reverse_string(string):
    return string[::-1]
