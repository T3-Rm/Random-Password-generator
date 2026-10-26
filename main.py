
import string
import secrets


CHARACTER_SETS = {
    "lowercase letters": string.ascii_lowercase,
    "uppercase letters": string.ascii_uppercase,
    "numbers": string.digits,
    "symbols": "!@#$%^&*()-_=+?",
}


def generate_password(length, selected_types):
    if not isinstance(length, int) or isinstance(length, bool):
        raise TypeError("Password length must be an integer.")
    if length < 8:
        raise ValueError("Password length must be at least 8.")

    selected_types = set(selected_types)
    if not selected_types.issubset(CHARACTER_SETS):
        raise ValueError("Selected character types are not supported.")
    if len(selected_types) < 2:
        raise ValueError("Select at least two character types.")

    characters = "".join(CHARACTER_SETS[kind] for kind in selected_types)
    required_characters = []

    for kind in selected_types:
        required_characters.append(secrets.choice(CHARACTER_SETS[kind]))

    # Fill the remaining password positions
    remaining = [
        secrets.choice(characters)
        for _ in range(length - len(required_characters))
    ]

    password_characters = required_characters + remaining

    # Shuffle characters securely
    secrets.SystemRandom().shuffle(password_characters)

    return "".join(password_characters)


def main():
    print("=" * 40)
    print("       RANDOM PASSWORD GENERATOR")
    print("=" * 40)

    while True:
        try:
            length = int(input("Enter password length (minimum 8): "))

            if length < 8:
                print("Error: Password length must be at least 8.")
                continue

            break

        except ValueError:
            print("Error: Please enter a whole number.")

    print("\nChoose at least TWO character types:")
    print("1. Lowercase letters (a-z)")
    print("2. Uppercase letters (A-Z)")
    print("3. Numbers (0-9)")
    print("4. Symbols (!@#$%^&*)")

    selected_types = {
        "1": "lowercase letters",
        "2": "uppercase letters",
        "3": "numbers",
        "4": "symbols",
    }

    while True:
        choices = input(
            "Enter your choices separated by commas (e.g. 1,2,3): "
        )
        chosen = {choice.strip() for choice in choices.split(",")}

        if not chosen.issubset(selected_types):
            print("Error: Choose only options 1, 2, 3, or 4.")
            continue

        if len(chosen) < 2:
            print("Error: Please select at least TWO character types.")
            continue

        break

    types = [selected_types[number] for number in chosen]

    while True:
        password = generate_password(length, types)

        print("\nYour generated password is:")
        print(password)

        again = input("\nGenerate another password? (y/n): ").lower()

        if again != "y":
            print("Thank you for using the Password Generator!")
            break


if __name__ == "__main__":
    main()
