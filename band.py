class Musician:
    instruments = ["guitar", "bass", "drums"]
    sounds = ["face melting guitar solo", "bom bom buh bom", "rattle boom crash"]

    def __init__(self, name):
        self.name = name

    def __str__(self):
        if self.name == 'Joan Jett':
            return f'My name is {self.name} and I play {Musician.instruments[0]}'
        elif self.name == 'Sheila E.':
            return f'My name is {self.name} and I play {Musician.instruments[2]}'
        else:
            return f'My name is {self.name} and I play {Musician.instruments[1]}'

    def __repr__(self):
        if self.name == 'Joan Jett':
            return f'Guitarist instance. Name = {self.name}'
        elif self.name == 'Sheila E.':
            return f'Drummer instance. Name = {self.name}'
        else:
            return f'Bassist instance. Name = {self.name}'

    def get_instrument(self):
        if self.name == 'Jimi Hendrix' or self.name == 'Kurt Cobain':
            return Musician.instruments[0]
        elif self.name == 'Flea' or self.name == 'Krist Novoselic':
            return Musician.instruments[1]
        else:
            return Musician.instruments[2]


class Guitarist(Musician):
    instrument = Musician.instruments[0]
    sound = Musician.sounds[0]

    def play_solo(self):
        return self.sound


class Bassist(Musician):
    instrument = Musician.instruments[1]
    sound = Musician.sounds[1]

    def play_solo(self):
        return self.sound


class Drummer(Musician):
    instrument = Musician.instruments[2]
    sound = Musician.sounds[2]

    def play_solo(self):
        return self.sound


class Band(Musician):
    solos = []
    instances = []

    def __init__(self, name, members):
        self.members = members
        self.instances.append(self)
        super(Band, self).__init__(name)

    def get_instrument(self):
        return self.members

    def play_solos(self):
        for member in self.members:
            self.solos.append(member.play_solo())
        return self.solos

    @classmethod
    def to_list(cls):
        return cls.instances