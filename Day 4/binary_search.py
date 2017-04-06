
class BinarySearch(list):
    def __init__(self, a, b):
        difference = b

        while len(self) < a:
            self.append(b)
            b += difference

        self.length = len(self)

    def search(self, value):
        first_index = 0
        last_index = len(self) - 1
        found = False
        count = 0

        if value not in self: #Check if the value given is in the list
            found = True
            value_index = -1

        
        if value == self[first_index]: #Checks if the value given is the first item in the list
            value_index = first_index
            found = True

        elif value == self[last_index]: #Checks if the value given is the last item in the list
            value_index = last_index
            found = True

        while first_index <= last_index and not found: #Carries out the binary search using while loop
            middle_index = (first_index + last_index) // 2
            if self[middle_index] == value:
                found = True
                value_index = middle_index
            else:
                count += 1  # Increment counter each time the process is undertaken
                if value < self[middle_index]:
                    last_index = middle_index - 1
                else:
                    first_index = middle_index + 1

        return {'count': count, 'index': value_index}


            
            
 
