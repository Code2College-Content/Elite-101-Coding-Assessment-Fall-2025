# Travel Buddy Chatbot

def main():
    print("Welcome to Travel Buddy — your virtual travel assistant!")
    name = input("What's your name? ")
    print(f"Hey {name}! Ready to explore some cool destinations today?")

    destinations = {
        "Paris": ["France", "The city of lights and love.", "Best time to visit: April to June."],
        "Tokyo": ["Japan", "A mix of high-tech and ancient traditions.", "Best time to visit: March to May."],
        "New York": ["USA", "The city that never sleeps.", "Best time to visit: September to November."],
        "Cancun": ["Mexico", "A tropical paradise with clear blue waters.", "Best time to visit: December to April."]
    }

    while True:
        print("\nWhat would you like to do?")
        print("1. View destinations")
        print("2. Get travel info")
        print("3. Exit")

        choice = input("Enter your choice (1–3): ")

        if choice == "1":
            print("\nAvailable Destinations:")
            for d in destinations.keys():
                print(f"- {d}")

        elif choice == "2":
            dest = input("Enter the name of the destination: ").strip().title()
            if dest in destinations:
                info = destinations[dest]
                print(f"\nDestination: {dest}")
                print(f"Country: {info[0]}")
                print(f"Description: {info[1]}")
                print(f"{info[2]}\n")
            else:
                print("Sorry, that destination isn't in our system yet!\n")

        elif choice == "3":
            print("Thanks for using Travel Buddy! Have a great day!")
            break

        else:
            print("Invalid choice. Please enter 1, 2, or 3.")

if __name__ == "__main__":
    main()
