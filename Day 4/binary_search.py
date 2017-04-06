
class BinarySearch(list):
    def __init__(self, a, b):
        difference = b

        while len(self) < a:
            self.append(b)
            b += difference

        self.length = len(self)

    def search(self, value):
        count = 0
        index = 0
        while self[index] is not value:
            index += 1
            count += 1

        return {'count': count, 'index': index}
            
            
            
 
