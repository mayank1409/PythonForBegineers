class Book :
    def __init__(self, name, noOfCopies):
        self.name = name
        self.noOfCopies = noOfCopies


    def increase_no_of_copies(self, copies):
        self.noOfCopies += copies


    def decrease_no_of_copies(self, copies):
        self.noOfCopies -= copies


    def __repr__(self):
        return repr(
            (self.name, self.noOfCopies)
        )


book1 = Book('Mastering Python', 10)
book2 = Book('Mastering Web Services', 20)

print(book1)
print(book2)
book1.increase_no_of_copies(5)
print(book1)
book2.decrease_no_of_copies(10)
print(book2)
