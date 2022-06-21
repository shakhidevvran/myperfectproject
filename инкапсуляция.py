class Car:
    def __init__(self, title, model, max_speed, speed):
        self.title = title
        self.model = model
        self.max_speed = max_speed
        self.speed = speed
        self._current_speed = 0

    def _get_current_speed(self):
        print(f"current speed {self._current_speed}")

    def start_engine(self):
        print(f"{self.title} {self.model} engine started")

    def gas(self):
        if self._current_speed + self.speed < self.max_speed:
            self._current_speed += self.speed
            self._get_current_speed()
        else:
            print("check on")

    def stop(self):
        if self._current_speed - self.speed > 0:
            self._current_speed -= self.speed
            self._get_current_speed()
        else:
            print("Check On")

bmw = Car('BMW', 'e38', 360, 20)
bmw.start_engine()
bmw.gas()
bmw.gas()