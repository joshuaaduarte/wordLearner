import csv
import random
import tkinter as tk
from tkinter import messagebox
from tkinter import NoDefaultRoot



def load_word_definitions():
    word_definitions = {}
    with open('wordList.csv', 'r') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            word = row['word']
            definition = row['definition']
            word_definitions[word] = definition
    return word_definitions

def get_random_word(word_definitions):
    return random.choice(list(word_definitions.keys()))


def show_random_word():
    word = get_random_word(word_definitions)
    definition = word_definitions.get(word)

    if definition:
        messagebox.showinfo("Word of the Day", f"{word}: {definition}")
    else:
        messagebox.showinfo("Word of the Day", word)


def create_window():
    window = tk.Tk()
    window.title("Word of the Day")
    window.geometry("300x200")
    window_width = 300
    window_height = 200
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    x = (screen_width // 2) - (window_width // 2)
    y = (screen_height // 2) - (window_height // 2)
    window.geometry(f"{window_width}x{window_height}+{x}+{y}")
    window.configure(bg="#F7F7F7")

    title_label = tk.Label(window, text="Word of the Day", font=("Arial", 16), bg="#F7F7F7")
    title_label.pack(pady=10)

    button = tk.Button(window, text="Get Word", font=("Arial", 12), command=show_random_word)
    button.pack(pady=20)

    window.mainloop()


# Load word definitions
word_definitions = load_word_definitions()

# Create the window
create_window()
