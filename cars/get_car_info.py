from create_car import Cars


def get_car_info(title, model, color):
    car = Cars(title=title, model=model, color=color)
    return car
