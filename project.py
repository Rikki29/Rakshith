import random

# Dictionary of quotes by category
quotes = {
    'motivation': [
        {"quote": "The only limit to our realization of tomorrow will be our doubts of today. ", "author": "Franklin D. Roosevelt"},
        {"quote": "Believe you can and you're halfway there. ", "author": "Theodore Roosevelt"},
        {"quote": "Don't watch the clock; do what it does. Keep going. ", "author": " Sam Levenson"},
        {"quote": "The future belongs to those who believe in the beauty of their dreams. - Eleanor Roosevelt"}
    ],
    'success': [
        {"quote": "The best way to predict the future is to create it. ", "author": " Peter Drucker"},
        {"quote": "The future depends on what you do today. ", "author": " Mahatma Gandhi"},
        {"quote": "The only way to do great work is to love what you do. ", "author": " Steve Jobs"},
        {"quote": "Success is not final, failure is not fatal: It is the courage to continue that counts. ", "author": " Winston Churchill"}
    ],
    'perseverance': [
        {"quote": "The harder the struggle, the more glorious the triumph. ", "author": " Anonymous"},
        {"quote": "Success is not how high you have climbed, but how you make a positive difference to the world. ", "author": " Roy T. Bennett"},
        {"quote": "The secret to success is to know something nobody else knows. ", "author": " Aristotle Onassis"},
        {"quote": "The future belongs to those who believe in the beauty of their dreams. ", "author": " Eleanor Roosevelt"}
    ]
}


def get_user_input(prompt):
    while True:
        user_input = input(prompt)
        if user_input.strip():
            return user_input.strip()
        print("Invalid input")


def generate_quote():
    name = get_user_input("Enter your name:")
    print()
    print("Select categories for quote:")
    categories = list(quotes.keys())
    for i, category in enumerate(categories, 1):
        print(f"{i}. {category.capitalize()}")

    while True:
        category_choice = get_user_input("Enter the category number:")
        if category_choice.isdigit() and 1 <= int(category_choice) <= len(categories):
            category = categories[int(category_choice) - 1]
            break
        print("Invalid category number")
    
    random_quote = random.choice(quotes[category])
    quote = random_quote["quote"]
    author = random_quote["author"]
    
    print(f"\n{name}, here is your quote:\n")
    print(quote)
    print(f"- {author}")


# Call the generate_quote function to run the script
generate_quote()
