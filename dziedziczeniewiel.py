class Czlowiek:

    pochodzenie = 'Ziemia'

class Polak:

    kraj = 'Polska'

class Pilkarz(Czlowiek, Polak):
    imie = 'Adam'

    def info(self):

        print('Pochodzenie:', self.pochodzenie)
        print('Kraj:', self.kraj)
        print('Imię:', self.imie)

pilkarz = Pilkarz()
