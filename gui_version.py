import random
import tkinter as tk
from tkinter import messagebox
from tkinter import PhotoImage

# Function to start the game and handle guess attempts
def start_game():
    global number_to_guess, attempts_left
    number_to_guess = random.randint(1, 100)
    attempts_left = 5
    attempts_label.config(text=f"Attempts left: {attempts_left}")
    result_label.config(text="", fg="black")
    hint_label.config(text="")
    guess_entry.delete(0, tk.END)

# Function to check the player's guess and give hints
def check_guess():
    global attempts_left
    try:
        guess = int(guess_entry.get())
    except ValueError:
        messagebox.showerror("Invalid input", "Please enter a valid number.")
        return

    attempts_left -= 1
    attempts_label.config(text=f"Attempts left: {attempts_left}")

    if guess < number_to_guess:
        result_label.config(text="Too low!", fg="blue")
        give_hint(guess)
    elif guess > number_to_guess:
        result_label.config(text="Too high!", fg="blue")
        give_hint(guess)
    else:
        result_label.config(text="🎉 Congratulations! You guessed it right! 🎉", fg="green")
        hint_label.config(text="")
        return

    if attempts_left == 0:
        result_label.config(text=f"Game over! The number was {number_to_guess}", fg="red")
        messagebox.showinfo("Game Over", f"Game over! The number was {number_to_guess}")
        start_game()

# Function to provide hints based on proximity to the correct number
def give_hint(guess):
    difference = abs(guess - number_to_guess)
    if difference <= 5:
        hint_label.config(text="🔥 You're very close! 🔥", fg="orange")
    elif difference <= 10:
        hint_label.config(text="😊 You're getting warmer!", fg="purple")
    else:
        hint_label.config(text="❄️ You're far off!", fg="gray")

# Set up the Tkinter window
window = tk.Tk()
window.title("Guess the Number")
window.geometry("450x500")
window.config(bg="#f0f8ff")  # Light blue background color
window.columnconfigure(0, weight=1)
window.rowconfigure([0, 1, 2, 3, 4, 5, 6, 7], weight=1)  # Make rows responsive

# Add an image to make it more interactive (optional)
try:
    img = PhotoImage(file="guess_icon.png")  # Replace with your image path
    img = img.subsample(3, 3)  # Scale down the image if necessary
    img_label = tk.Label(window, image=img, bg="#f0f8ff")
    img_label.grid(row=0, column=0, pady=10, sticky="n")
except Exception as e:
    print(f"Image could not be loaded: {e}")

# Add instructions label with styling
instructions_label = tk.Label(window, text="Guess a number between 1 and 100:",
                              font=("Helvetica", 14, "bold"), bg="#f0f8ff", fg="#333")
instructions_label.grid(row=1, column=0, pady=10, sticky="n")

# Add entry widget for guessing the number
guess_entry = tk.Entry(window, width=10, font=("Helvetica", 12))
guess_entry.grid(row=2, column=0, pady=10, sticky="n")

# Add button to submit the guess with styling
submit_button = tk.Button(window, text="Submit Guess", command=check_guess, font=("Helvetica", 12),
                          bg="#ffebcd", fg="#333", activebackground="#ff4500", activeforeground="white")
submit_button.grid(row=3, column=0, pady=10, sticky="n")

# Add a label to display remaining attempts with custom font
attempts_label = tk.Label(window, text="Attempts left: 5", font=("Helvetica", 12), bg="#f0f8ff", fg="#333")
attempts_label.grid(row=4, column=0, pady=10, sticky="n")

# Add a label to display results with larger font and color change
result_label = tk.Label(window, text="", font=("Helvetica", 14, "bold"), bg="#f0f8ff")
result_label.grid(row=5, column=0, pady=20, sticky="n")

# Add a label to display hints based on proximity
hint_label = tk.Label(window, text="", font=("Helvetica", 12, "italic"), bg="#f0f8ff", fg="gray")
hint_label.grid(row=6, column=0, pady=10, sticky="n")

# Add a button to start a new game with hover effects
def on_enter(e):
    new_game_button.config(bg="#008b8b", fg="white")

def on_leave(e):
    new_game_button.config(bg="#20b2aa", fg="black")

new_game_button = tk.Button(window, text="New Game", command=start_game, font=("Helvetica", 12),
                            bg="#20b2aa", fg="black", activebackground="#008b8b", activeforeground="white")
new_game_button.grid(row=7, column=0, pady=20, sticky="n")

# Add hover effects for new game button
new_game_button.bind("<Enter>", on_enter)
new_game_button.bind("<Leave>", on_leave)

# Initialize the game
start_game()

# Run the Tkinter event loop
window.mainloop()
