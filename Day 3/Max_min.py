def find_max_min(n):
    if type(n) is not list:
        return "Invalid input, only lists allowed"

    else:
        if max(n) == min(n):
            output = [len(n)]

        else:
            highest = max(n)
            lowest = min(n)
            output = [lowest, highest]

        return output

