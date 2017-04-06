def find_missing(lista, listb):
    
    if type(lista) is list: #Checks if input given is a list
        if type(listb) is list: #Checks if input given is a list
            
            result = set(listb) - set(lista) #Finds the difference of elements in the two lists
            
            if result == set(): # returns 0 if the lists have the same elements or the an empty list was given
                return(0)

            else:
                for data in result:#returns the missing number(s)
                    return data

