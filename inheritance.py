class Pet:
    """Serves as a base class for creating Pet objects.
    A Pet is initialized with a name, a gender, and a species."""

    def __init__(self, name, gender, species):
        self.name = name
        self.gender = gender
        self.species = species

    def __str__(self):
        """Returns a string representation of the animal's name and species."""
        return f"{self.name} is a {self.species}."

    def make_sound(self, sound):
        return f"This animal makes the sound: {sound}."

class Cat(Pet):
    """Creates an instance of the Cat class which inherits from the Pet class. A Cat is initialized with attributes for a name, gender, breed, and a toy they like to play with."""

    def __init__(self, name, gender, breed, toy):
        Pet.__init__(self, name, gender, species='cat')
        self.breed = breed
        self.toy = toy

    def play(self):
        return f"{self.name} plays with {self.toy}."

    def chase_bird(self):
        return f"{self.name} chases a bird."

class Dog(Pet):
    """Creates an instance of the Dog class which inherits from the Pet class. A Dog is initialized with attributes for a name, gender, breed, and a toy they like to play with."""

    def __init__(self, name, gender, breed, toy):
        Pet.__init__(self, name, gender, species='dog')
        self.breed = breed
        self.toy = toy

    def play(self):
        return f"{self.name} plays with {self.toy}."

    def chase_cat(self):
        return f"{self.name} chases a cat."

class Bird(Pet):
    """Creates an instance of the Bird class which inherits from the Pet class. A Bird is initialized with attributes for a name, gender, breed, and whether they can fly."""

    def __init__(self, name, gender, breed, can_fly):
        Pet.__init__(self, name, gender, species='bird')
        self.breed = breed
        self.can_fly = can_fly

    def play(self):
        return f"{self.name} chases its friends."

    def fly_away(self):
        """Returns a string saying whether a bird can fly."""
        if self.can_fly:
            return f"{self.name} flies away."
        else:
            return f"{self.name} can't fly."


# TEST DATA

# create new instance of Cat
new_cat = Cat('Buzzsaw', 'Male', 'Tabby', 'string')
print(new_cat.name)
print(new_cat.species)
print(new_cat.gender)
print(new_cat.breed)
print(new_cat.toy)
print()
print(new_cat)
print(new_cat.make_sound('meow'))
print(new_cat.play())
print(new_cat.chase_bird())
print()

# create new instance of Dog
new_dog = Dog('Dojo', 'Male', 'Dalmation', 'ball')
print(new_dog)
print(new_dog.make_sound('ruff'))
print(new_dog.play())
print(new_dog.chase_cat())
print()

# create new instance of Bird
new_bird = Bird('Polly', 'Female', 'Parakeet', True)
print(new_bird)
print(new_bird.make_sound('chirp'))
print(new_bird.play())
print(new_bird.fly_away())
