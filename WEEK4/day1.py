class Person:

    def __init__(self, gender, skin_type):
        self.gender = gender
        self.skin_type = skin_type

    legs = 2
    ears = 2

    def get_gender(self):
        return f"This person is a {self.gender}"
    
    def get_skintype(self):
        return f"This person has a skin type of {self.skin_type}"

    def set_skin_type(self, new_skin_type):
        self.skin_type = new_skin_type
        return f"The person's new skin type is {self.skin_type}"


dan = Person("male", "black")
maurine = Person("female", "black")

print(maurine.set_skin_type("brown"))
print(maurine.get_skintype())