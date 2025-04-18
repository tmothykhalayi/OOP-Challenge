from Pet import Pet

def main():
    # Create a pet named Max
    max_pet = Pet("Max")
    
    # Test the pet's actions
    max_pet.eat()
    max_pet.play()
    max_pet.sleep()

    # Print the current status of the pet
    max_pet.get_status()
    
    # Teach Max some tricks
    max_pet.train("roll over")
    max_pet.train("play dead")
    
    # Show all tricks
    max_pet.show_tricks()

    # Print the final status of Max
    max_pet.get_status()

if __name__ == "__main__":
    main()
