class Dog:
    # Constructor
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed
 
    # Instance method
    def bark(self):
        return f"{self.name} says: Woof!"
 
    def info(self):
        return f"{self.name} is a {self.breed}"
 
# Create instances (objects)
dog1 = Dog("Rex", "Labrador")
dog2 = Dog("Buddy", "Poodle")
 
print(dog1.bark())    # Rex says: Woof!
print(dog2.info())    # Buddy is a Poodle
 
# Access attributes
print(dog1.name)      # Rex
dog1.age = 3          # Add attribute dynamically
print(dog1.age)       # 3