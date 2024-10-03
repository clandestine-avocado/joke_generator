import requests
import time

def get_joke():
    url = "https://official-joke-api.appspot.com/random_joke"
    response = requests.get(url)
    if response.status_code == 200:
        joke_data = response.json()
        return f"{joke_data['setup']}\n\n{joke_data['punchline']}"
    else:
        return "Failed to fetch a joke. Please try again."

def main():
    print("Welcome to the Random Joke Generator!")
    print("Press Enter to get a new joke or 'q' to quit.")

    while True:
        user_input = input("\nPress Enter for a joke or 'q' to quit: ")
        if user_input.lower() == 'q':
            print("Thanks for laughing with us! Goodbye!")
            break

        print("\nFetching a joke for you...")
        joke = get_joke()
        print("\n" + joke)
        time.sleep(2)  # Pause for 2 seconds before allowing the next joke

if __name__ == "__main__":
    main()
    