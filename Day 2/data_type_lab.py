def data_type(n):
    if isinstance(n, str):
        return (len(n))

    elif n is None:
        return 'no value'

    elif n is True or False:
        return n

    elif isinstance(n, int):
        if n > 100:
            return "more than 100"

        elif n == 100:
            return "equal to 100"

        else:
            return "less than 100"

    elif type(n) is list:
        if len(n) < 3:
            return None

        else:
            return n[2]



    
