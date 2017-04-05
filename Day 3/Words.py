def words(n):
    split_string = n.split()
    output_dictionary ={}

    for item in split_string:
        count = split_string.count(item)
        
        if item.isdigit():
            item = int(item)


            
        output_dictionary[item] = count
        
    return(output_dictionary)

