class Person:

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def info(self):
        print(f"""
        first name: {self.first_name}
        last name: {self.last_name}
        age: {self.age}
        
        """)
