import tkinter as tk
from tkinter import messagebox
import requests
import threading

class JokeGenerator:
    def __init__(self):
        self.setup = ""
        self.punchline = ""

    def get_joke(self):
        url = "https://official-joke-api.appspot.com/random_joke"
        try:
            response = requests.get(url)
            if response.status_code == 200:
                joke_data = response.json()
                self.setup = joke_data['setup']
                self.punchline = joke_data['punchline']
                return True
            else:
                self.setup = "Failed to fetch a joke. Please try again."
                self.punchline = ""
                return False
        except requests.RequestException:
            self.setup = "Network error. Please check your internet connection."
            self.punchline = ""
            return False

def fetch_joke_thread():
    joke_text.set("Fetching a joke...")
    punchline_text.set("")
    success = joke_generator.get_joke()
    joke_text.set(joke_generator.setup)
    if success:
        reveal_button.config(state=tk.NORMAL)
    else:
        reveal_button.config(state=tk.DISABLED)
    joke_button.config(state=tk.NORMAL)

def update_joke():
    joke_button.config(state=tk.DISABLED)
    reveal_button.config(state=tk.DISABLED)
    threading.Thread(target=fetch_joke_thread).start()

def reveal_punchline():
    punchline_text.set(joke_generator.punchline)
    reveal_button.config(state=tk.DISABLED)

# Create the main window
root = tk.Tk()
root.title("Random Joke Generator")
root.geometry("400x350")
root.configure(bg="#f0f0f0")

# Initialize JokeGenerator
joke_generator = JokeGenerator()

# Create and pack the title label
title_label = tk.Label(root, text="Random Joke Generator", font=("Arial", 16, "bold"), bg="#f0f0f0")
title_label.pack(pady=20)

# Create and pack the joke setup display
joke_text = tk.StringVar()
joke_text.set("Click 'Get New Joke' to start!")
joke_display = tk.Label(root, textvariable=joke_text, wraplength=350, font=("Arial", 12), bg="#f0f0f0")
joke_display.pack(expand=True, fill=tk.BOTH, padx=20)

# Create and pack the punchline display
punchline_text = tk.StringVar()
punchline_display = tk.Label(root, textvariable=punchline_text, wraplength=350, font=("Arial", 12, "italic"), bg="#f0f0f0", fg="#1a1a1a")
punchline_display.pack(expand=True, fill=tk.BOTH, padx=20)

# Create and pack the buttons
button_frame = tk.Frame(root, bg="#f0f0f0")
button_frame.pack(pady=20)

joke_button = tk.Button(button_frame, text="Get New Joke", command=update_joke, font=("Arial", 12), bg="#4CAF50", fg="white")
joke_button.pack(side=tk.LEFT, padx=10)

reveal_button = tk.Button(button_frame, text="Reveal Punchline", command=reveal_punchline, font=("Arial", 12), bg="#2196F3", fg="white", state=tk.DISABLED)
reveal_button.pack(side=tk.LEFT, padx=10)

# Start the GUI event loop
root.mainloop()