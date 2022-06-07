# class User:
#
#
#     def __init__(self, first_name, last_name, age):
#         self.first_name = first_name
#         self.last_name = last_name
#         self.age = age это атрибуты
#
# jack = User('Jack', 'Barbaro', 20) #является экземпляром класса User
# print(jack.first_name, jack.last_name, jack.age)

# class Car:
#     def __init__(self, title, module, color):
#         self.title = title
#         self.module = module
#         self.color = color
#
# cars = Car("mers", 'v34', 'red')
# print(cars.title,cars.module,cars.color)

class Car:
    def __init__(self, title, model, engine, max_speed, speed):
        self.title = title
        self.model = model
        self.engine = engine
        self.max_speed = max_speed
        self.speed = speed
        self.current_speed = 0


    def get_info(self):
        print(f"""
Title: {self.title} {self.model}
Engine: {self.engine}
Max Sreed: {self.max_speed}
        """)

    def gas(self):
        if self.current_speed + self.speed >= self.max_speed:
            print("check on")
        else:
            self.current_speed += self.speed
            print(f"Current speed = {self.current_speed}")

bmw = Car('BMW', "e38", 'v10', 360, 20)
bmw.get_info()
bmw.gas()

mercedes = Car('mers', "s500", "v10", 360, 15)
mercedes.get_info()
mercedes.gas()