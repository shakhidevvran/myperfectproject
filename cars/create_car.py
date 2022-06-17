class Car:
    def __init__(self, title, model):
        self.title = title
        self.model = model


class Cars(Car):
    def __init__(self, title, model, color):
        super().__init__(title, model)
        self.color = color

    def start_engine(self):
        print(f'On {self.title} {self.model} {self.color} engine!')

    def stop_engine(self):
        print(f'Off {self.title} {self.model} {self.color} engine!')
