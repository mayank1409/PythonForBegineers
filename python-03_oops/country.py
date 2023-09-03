class Country:
    def __init__(self, name):
        self.name = name

    def print_name(self):
        print(self.name)

    def __repr__(self):
        return repr(
            (self.name)
        )

india = Country('INDIA')
australia = Country('AUSTRALIA')
usa = Country('USA')

india.print_name()
australia.print_name()
usa.print_name()