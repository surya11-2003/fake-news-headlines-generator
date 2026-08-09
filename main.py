import random

subjects = [
    "A Bollywood Actor",
    "A Cricket Player",
    "A Government Official",
    "A Mumbai Cat",
    "A Group of Monkeys",
    "An Auto Driver",
    "A Bollywood Director",
    "An IIT Student"
]

actions = [
    "launches",
    "cancels",
    "dances with",
    "eats",
    "declares war on",
    "buys",
    "sells",
    "hides",
    "celebrates",
    "invests in"
]

places = [
    "at Red Fort",
    "in Mumbai local train",
    "a plate of samosas",
    "inside Parliament",
    "at Ganga ghat",
    "in Chandni Chowk",
    "near India Gate",
    "a cricket stadium",
    "a tea stall",
    "during a wedding procession"
]

print("=== Fake News Headline Generator ===")

while True:
    subject = random.choice(subjects)
    action = random.choice(actions)
    place = random.choice(places)

    headline = f"BREAKING: {subject} {action} {place}!"

    print("\n" + headline)

    choice = input(
        "\nGenerate another headline? (yes/no): "
    ).lower()

    if choice == "no":
        break

print("\nThank you for using the Fake News Headline Generator!")