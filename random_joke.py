import tkinter as tk
from tkinter import messagebox
import requests
import threading

def get_joke():
    url = "https://official-joke-api.appspot.com/random_joke"
    try:
        response = requests.get(url)
        if response.status_code == 200:
            joke_data = response.json()
            return f"{joke_data['setup']}\n\n{joke_data['punchline']}"
        else:
            return "Failed to fetch a joke. Please try again."
    except requests.RequestException:
        return "Network error. Please check your internet connection."

def fetch_joke_thread():
    joke.set("Fetching a joke...")
    new_joke = get_joke()
    joke.set(new_joke)
    joke_button.config(state=tk.NORMAL)

def update_joke():
    joke_button.config(state=tk.DISABLED)
    threading.Thread(target=fetch_joke_thread).start()

# Create the main window
root = tk.Tk()
root.title("Random Joke Generator")
root.geometry("400x300")
root.configure(bg="#f0f0f0")

# Create and pack the title label
title_label = tk.Label(root, text="Random Joke Generator", font=("Arial", 16, "bold"), bg="#f0f0f0")
title_label.pack(pady=20)

# Create and pack the joke display
joke = tk.StringVar()
joke.set("Click the button to get a joke!")
joke_display = tk.Label(root, textvariable=joke, wraplength=350, font=("Arial", 12), bg="#f0f0f0")
joke_display.pack(expand=True, fill=tk.BOTH, padx=20)

# Create and pack the button
joke_button = tk.Button(root, text="Get New Joke", command=update_joke, font=("Arial", 12), bg="#4CAF50", fg="white")
joke_button.pack(pady=20)

# Start the GUI event loop
root.mainloop()