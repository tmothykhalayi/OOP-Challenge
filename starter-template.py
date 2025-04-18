class Pet:
    def __init__(self, name):
        self.name = name 
        self.hunger = 5  # 0 is very hungry, 10 is full
        self.energy = 5  # 0 is very tired, 10 is fully rested
        self.happiness = 5  # 0 is unhappy, 10 is very happy
        self.tricks = []  # List of tricks the pet knows

    def eat(self):
        if self.hunger < 10:
            self.hunger += 2  # Eating restores hunger
            if self.hunger > 10:
                self.hunger = 10  # Ensure hunger doesn't exceed 10
            print(f"{self.name} is eating. Hunger level: {self.hunger}")
        else:
            print(f"{self.name} is not hungry!")

    def sleep(self):
        if self.energy < 10:
            self.energy += 3  # Sleeping restores energy
            if self.energy > 10:
                self.energy = 10  # Ensure energy doesn't exceed 10
            print(f"{self.name} is sleeping. Energy level: {self.energy}")
        else:
            print(f"{self.name} is not tired!")

    def play(self):
        if self.energy > 1 and self.hunger < 9:
            self.energy -= 2  # Playing consumes energy
            self.happiness += 1  # Playing increases happiness
            self.hunger += 1  # Playing makes the pet a bit hungrier
            print(f"{self.name} is playing. Happiness level: {self.happiness}, Hunger level: {self.hunger}")
        else:
            print(f"{self.name} is too tired or hungry to play!")

    def train(self, trick):
        if self.energy > 2 and self.happiness > 3:
            self.energy -= 1  # Training consumes some energy
            self.happiness += 1  # Training can increase happiness
            self.tricks.append(trick)  # Adds the new trick
            print(f"{self.name} learned a new trick: {trick}!")
        else:
            print(f"{self.name} is not in the right condition to train!")

    def show_tricks(self):
        if self.tricks:
            print(f"{self.name} can do the following tricks: {', '.join(self.tricks)}")
        else:
            print(f"{self.name} doesn't know any tricks yet!")

    def get_status(self):
        print(f"{self.name}'s Status:")
        print(f"Hunger: {self.hunger}")
        print(f"Energy: {self.energy}")
        print(f"Happiness: {self.happiness}")
        print(f"Tricks: {', '.join(self.tricks) if self.tricks else 'No tricks learned yet'}")
