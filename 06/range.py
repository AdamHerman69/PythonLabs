def my_range(*args):
    if (len(args) > 3 or len(args) == 0):
        raise ValueError()
    elif (len(args) == 1):
        start = 0;
        limit = args[0]
        step = 1
    elif (len(args) == 2):
        start = args[0]
        limit = args[1]
        step = 1
    elif (len(args) == 3):
        start = args[0]
        limit = args[1]
        step = args[2]

    range = []
    while start < limit:
        range.append(start)
        start += step
    return range
