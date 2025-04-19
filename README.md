# 🐶 Python OOP Challenge: Build Your Own Digital Pet
Welcome to this week's Python challenge! 🎉

In this challenge, you’ll be creating a virtual pet using Object-Oriented Programming concepts in Python. This fun project will help you practice how to use classes, attributes, methods, and constructors.

---

## 🧠 Objective

Create a class called `Pet` with the following:

### Attributes:
- `name`: the name of your pet
- `hunger`: an integer representing hunger level (0 = full, 10 = very hungry)
- `energy`: an integer representing energy level (0 = tired, 10 = fully rested)
- `happiness`: an integer (0–10)

### Methods:
- `eat()`: reduces hunger by 3 points (but not below 0), and increases happiness by 1.
- `sleep()`: increases energy by 5 points (but not above 10).
- `play()`: decreases energy by 2, increases happiness by 2, and increases hunger by 1.
- `get_status()`: prints the current state of the pet.

### Bonus 🎯
- Add a method `train(trick)` that teaches your pet a new trick and stores it in a list.
- Add a method `show_tricks()` that prints all learned tricks.

---

## 📝 How to Complete

1. Fork or clone this repo.
2. Write your `Pet` class in `pet.py`.
3. In `main.py`, create a pet object and call its methods to test functionality.
4. Submit a GitHub repo or a zipped folder with your code and a screenshot of the output.

---

## ✅ Sample Output

```bash
Creating pet: Max
Max is eating...
Max is playing...
Max is sleeping...
Max's current status:
Hunger: 2
Energy: 8
Happiness: 9
Tricks: ['roll over', 'play dead']


### 💡 Tips
Use max() and min() to keep values between 0 and 10.

Think about edge cases like trying to play when energy is 0.

🏁 Submission
Deadline: [Set your date]

Submission format: clone / fork this repo

Bonus points for creativity (custom actions, emojis, pet types, etc.)

sample output 
![alt text](<WhatsApp Image 2025-04-18 at 16.03.36_89745ad7.jpg>)