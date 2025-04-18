# week1.py

from starter_template import Pet  # Import the Pet class from starter_template.py

def main():
    # Create a pet named "Buddy"
    pet = Pet("Buddy")

    # Show initial status
    pet.get_status()

    # Interact with the pet
    pet.eat()  # Buddy eats
    pet.sleep()  # Buddy sleeps
    pet.play()  # Buddy plays
    pet.train("roll over")  # Buddy learns a new trick
    pet.show_tricks()  # Show Buddy's tricks

    # Show updated status
    pet.get_status()

if __name__ == "__main__":
    main()
