# IS A

# A Student(college, yearOfGraduation, degree) 
# IS A Person(name, address)

class Person:
    def __init__(self, name, address):
        self.name = name
        self.address = address

    def __repr__(self):
        return repr(
            (self.name, self.address)
        )


class Student(Person):
    def __init__(self, name, address, college, yearOfGraduation, degree):
        super().__init__(name, address)
        self.college = college
        self.yearOfGraduation = yearOfGraduation
        self.degree = degree

    def __repr__(self):
        return repr(
            (super().__repr__(), self.college, self.yearOfGraduation, self.degree)
        )


ranga = Person('Ranga', 'Hyderabad')
print(ranga)

student = Student(ranga.name, ranga.address, 'IIIT Hyderabad', 1994, 'CSE')
print(student)
