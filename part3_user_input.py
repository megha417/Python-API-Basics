"""
Part 3: Dynamic Queries with User Input
=======================================
Difficulty: Intermediate

Learn:
- Using input() to make dynamic API requests
- Building URLs with f-strings
- Query parameters in URLs
"""

""" import requests


def get_user_info():
    
    print("=== User Information Lookup ===\n")

    user_id = input("Enter user ID (1-10): ")

    url = f"https://jsonplaceholder.typicode.com/users/{user_id}"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        print(f"\n--- User #{user_id} Info ---")
        print(f"Name: {data['name']}")
        print(f"Email: {data['email']}")
        print(f"Phone: {data['phone']}")
        print(f"Website: {data['website']}")
    else:
        print(f"\nUser with ID {user_id} not found!")


def search_posts():
    Search posts by user ID.
    print("\n=== Post Search ===\n")

    user_id = input("Enter user ID to see their posts (1-10): ")

    # Using query parameters
    url = "https://jsonplaceholder.typicode.com/posts"
    params = {"userId": user_id}

    response = requests.get(url, params=params)
    posts = response.json()

    if posts:
        print(f"\n--- Posts by User #{user_id} ---")
        for i, post in enumerate(posts, 1):
            print(f"{i}. {post['title']}")
    else:
        print("No posts found for this user.")


def get_crypto_price():
    Fetch cryptocurrency price based on user input.
    print("\n=== Cryptocurrency Price Checker ===\n")

    print("Available coins: btc-bitcoin, eth-ethereum, doge-dogecoin")
    coin_id = input("Enter coin ID (e.g., btc-bitcoin): ").lower().strip()

    url = f"https://api.coinpaprika.com/v1/tickers/{coin_id}"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        price_usd = data['quotes']['USD']['price']
        change_24h = data['quotes']['USD']['percent_change_24h']

        print(f"\n--- {data['name']} ({data['symbol']}) ---")
        print(f"Price: ${price_usd:,.2f}")
        print(f"24h Change: {change_24h:+.2f}%")
    else:
        print(f"\nCoin '{coin_id}' not found!")
        print("Try: btc-bitcoin, eth-ethereum, doge-dogecoin")


def main():
    Main menu for the program.
    print("=" * 40)
    print("  Dynamic API Query Demo")
    print("=" * 40)

    while True:
        print("\nChoose an option:")
        print("1. Look up user info")
        print("2. Search posts by user")
        print("3. Check crypto price")
        print("4. Exit")

        choice = input("\nEnter choice (1-4): ")

        if choice == "1":
            get_user_info()
        elif choice == "2":
            search_posts()
        elif choice == "3":
            get_crypto_price()
        elif choice == "4":
            print("\nGoodbye!")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main() 
"""


# --- EXERCISES ---
#
# Exercise 1: Add a function to fetch weather for a city
#             Use Open-Meteo API (no key required):
#             https://api.open-meteo.com/v1/forecast?latitude=28.61&longitude=77.23&current_weather=true
#             Challenge: Let user input city name (you'll need to find lat/long)
#
# Exercise 2: Add a function to search todos by completion status
#             URL: https://jsonplaceholder.typicode.com/todos
#             Params: completed=true or completed=false
#
# Exercise 3: Add input validation (check if user_id is a number)

"""
Part 3: Dynamic Queries with User Input + Exercises
==================================================
Difficulty: Intermediate
"""

"""
Exercise 1: Fetch weather for a city using Open-Meteo API
Cities include Pune.
"""

import requests

# Predefined city coordinates
CITY_COORDS = {
    "delhi": {"latitude": 28.61, "longitude": 77.23},
    "mumbai": {"latitude": 19.07, "longitude": 72.87},
    "bangalore": {"latitude": 12.97, "longitude": 77.59},
    "chennai": {"latitude": 13.08, "longitude": 80.27},
    "pune": {"latitude": 18.52, "longitude": 73.85}  # Added Pune
}

def get_weather():
    """Fetch current weather for a city from the list."""
    print("=== Weather Checker ===\n")
    print("Available cities:", ", ".join(CITY_COORDS.keys()))
    city = input("Enter city name: ").lower().strip()

    if city not in CITY_COORDS:
        print("City not found! Please choose from the list.")
        return

    coords = CITY_COORDS[city]
    url = "https://api.open-meteo.com/v1/forecast"
    params = {
        "latitude": coords["latitude"],
        "longitude": coords["longitude"],
        "current_weather": "true"
    }
    response = requests.get(url, params=params)

    if response.status_code == 200:
        data = response.json()
        temp = data['current_weather']['temperature']
        wind = data['current_weather']['windspeed']

        print(f"\n--- Current Weather in {city.title()} ---")
        print(f"Temperature: {temp}°C")
        print(f"Wind Speed: {wind} km/h")
    else:
        print("Weather data could not be retrieved.")

if __name__ == "__main__":
    get_weather()

"""
Exercise 2: Search todos by completion status
"""



def search_todos():
    """Fetch todos based on completion status."""
    print("=== Todos Search ===\n")
    status = input("Show completed or not completed todos? (true/false): ").lower().strip()

    if status not in ["true", "false"]:
        print("Invalid input! Enter 'true' or 'false'.")
        return

    url = "https://jsonplaceholder.typicode.com/todos"
    params = {"completed": status}
    response = requests.get(url, params=params)
    todos = response.json()

    if todos:
        print(f"\n--- Todos with completed={status} ---")
        for todo in todos[:10]:  # show only first 10 for brevity
            print(f"[{'✓' if todo['completed'] else '✗'}] {todo['title']}")
    else:
        print("No todos found for this status.")

if __name__ == "__main__":
    search_todos()


"""
Exercise 3: Input validation for user ID
"""

def get_user_id():
    """Prompt user for a valid user ID (1-10)."""
    user_id = input("Enter user ID (1-10): ").strip()

    # Check if input is a number
    if not user_id.isdigit():
        print("Invalid input! Please enter a number.")
        return None

    # Convert to integer and check range
    user_id = int(user_id)
    if not (1 <= user_id <= 10):
        print("Invalid user ID! Must be between 1 and 10.")
        return None

    print(f"Valid user ID entered: {user_id}")
    return user_id


if __name__ == "__main__":
    get_user_id()

"""
Exercise 3: Input validation for user ID
"""

def get_user_id():
    """Prompt user for a valid user ID (1-10)."""
    user_id = input("Enter user ID (1-10): ").strip()

    # Check if input is a number
    if not user_id.isdigit():
        print("Invalid input! Please enter a number.")
        return None

    # Convert to integer and check range
    user_id = int(user_id)
    if not (1 <= user_id <= 10):
        print("Invalid user ID! Must be between 1 and 10.")
        return None

    print(f"Valid user ID entered: {user_id}")
    return user_id


if __name__ == "__main__":
    get_user_id()
