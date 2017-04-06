def find_missing(lista, listb):
    if type(lista) is list:
        if type(listb) is list:
            result = set(listb) - set(lista)
            if result == set():
                return(0)

            else:
                for data in result:
                    return data

