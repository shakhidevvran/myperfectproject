class Bmw:
    def __init__(self, title, model, weight, hp, nm, max_speed, color):
        self.title = title
        self.model = model
        self.weight = weight
        self.hp = hp
        self.nm = nm
        self.max_speed = max_speed
        self.color = color

    def start_engine(self):
        print(f'{self.title} {self.model} engine started!')

    def stop_engine(self):
        print(f'{self.title} {self.model} engine stopped!')

    def info(self):
        print(f'All info: {bmw.title} {bmw.model} {bmw.weight} {bmw.hp} {bmw.nm} {bmw.max_speed} {bmw.color}\n')


bmw = Bmw("bmw", 'x5', '2100kg', '184l', '400nm', '360', 'black')
bmw.start_engine()
bmw.stop_engine()
bmw.info()


class Mers:
    def __init__(self, title, model, weight, hp, nm, max_speed, color):
        self.title = title
        self.model = model
        self.weight = weight
        self.hp = hp
        self.nm = nm
        self.max_speed = max_speed
        self.color = color

    def start_engine(self):
        if self.title + self.model:
            print(f'{self.title} {self.model} engine started!')

    def stop_engine(self):
        if self.title + self.model:
            print(f'{self.title} {self.model} engine stopped!')

    def info(self):
        print(f'All info: {mers.title} {mers.model} {mers.weight} {mers.hp} {mers.nm} {mers.max_speed} {mers.color}')


mers = Mers("Mercedes", 'AMG GP', '2195kg', '520l', '476nm', '380', 'grey')
mers.start_engine()
mers.stop_engine()
mers.info()
