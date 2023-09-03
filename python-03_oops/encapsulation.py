class BookEnhanced:
    def __init__(self, name, _copies):
        self.name = name
        self._copies = _copies

    @property
    def copies(self):
        print('getter called')
        return self._copies
    
    @copies.setter
    def copies(self, copies):
        print('setter called')
        if (copies >= 0):
            self._copies = copies

    
microservice = BookEnhanced('Microservice', 4)
print(microservice.copies)

microservice.copies = 10
print(microservice.copies)
