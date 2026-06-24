questions = {
    "Software": [
        "Explain OOP concepts",
        "Difference between Stack and Queue",
        "What is SQL?"
    ],
    "Core ECE": [
        "Explain DSP basics",
        "What is Embedded System?",
        "Explain ARM architecture"
    ]
}

completed = []


while True:
    print("\n=== Smart Interview Preparation Assistant ===")
    print("1. Select Role")
    print("2. View Progress")
    print("3. Exit")

    choice = input("Enter choice: ")

    if choice == "1":

        print("\nRoles:")
        print("1. Software")
        print("2. Core ECE")

        role = input("Select role: ")

        if role == "1":
            selected = "Software"

        elif role == "2":
            selected = "Core ECE"

        else:
            print("Invalid")
            continue

        print("\nQuestions:")

        for i, q in enumerate(questions[selected], start=1):
            print(f"{i}. {q}")

        done = input(
            "\nEnter completed question number (0 to skip): "
        )

        if done.isdigit():

            done = int(done)

            if done > 0 and done <= len(
                    questions[selected]):

                completed.append(
                    questions[selected][done - 1]
                )

                print("Progress Updated")

    elif choice == "2":

        print("\nCompleted Topics:")

        if len(completed) == 0:
            print("No progress yet")

        else:
            for item in completed:
                print("-", item)

    elif choice == "3":

        print("Good luck for placements!")
        break

    else:
        print("Invalid choice")
