class Player:
    count = 0 #static data member

    def __init__(self, name):
        self.name = name
        Player.count += 1


    @staticmethod
    def get_count():
        return Player.count


    def __repr__(self):
        return repr(
            (self.name)
        )
    
messi = Player('Messi')
rolando = Player('Rolando')

print('Total players count is ', Player.get_count())
