class Pet:
    def __init__(self, name):
        self.name = name
        self.hunger = 5  # Default hunger level
        self.energy = 5  # Default energy level
        self.happiness = 5  # Default happiness level
        self.tricks = []  # List to store tricks

    def eat(self):
        """Reduces hunger and increases happiness."""
        if self.hunger > 0:
            self.hunger = max(0, self.hunger - 3)
            self.happiness = min(10, self.happiness + 1)
            print(f"{self.name} is eating...")
        else:
            print(f"{self.name} is not hungry!")

    def sleep(self):
        """Increases energy."""
        self.energy = min(10, self.energy + 5)
        print(f"{self.name} is sleeping...")

    def play(self):
        """Decreases energy and increases happiness and hunger."""
        if self.energy > 0:
            self.energy = max(0, self.energy - 2)
            self.happiness = min(10, self.happiness + 2)
            self.hunger = min(10, self.hunger + 1)
            print(f"{self.name} is playing...")
        else:
            print(f"{self.name} is too tired to play!")

    def get_status(self):
        """Prints the current state of the pet."""
        print(f"{self.name}'s current status:")
        print(f"Hunger: {self.hunger}")
        print(f"Energy: {self.energy}")
        print(f"Happiness: {self.happiness}")
        if self.tricks:
            print(f"Tricks: {', '.join(self.tricks)}")
        else:
            print("Tricks: None")

    def train(self, trick):
        """Teaches a new trick."""
        self.tricks.append(trick)
        print(f"{self.name} learned a new trick: {trick}")

    def show_tricks(self):
        """Shows all learned tricks."""
        if self.tricks:
            print(f"{self.name} knows the following tricks: {', '.join(self.tricks)}")
        else:
            print(f"{self.name} doesn't know any tricks yet.")
