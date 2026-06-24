topics = {

    "ECE Core": {
        "Digital Signal Processing":
            "Study sampling, convolution and filtering.",

        "Embedded Systems":
            "Learn microcontrollers, memory and interfacing.",

        "Microcontrollers":
            "Understand ARM and STM32 basics.",

        "VLSI Basics":
            "Study CMOS and digital design.",

        "Communication Systems":
            "Learn AM, FM and modulation."
    },

    "Software": {

        "Data Structures":
            "Study arrays, stacks, queues and trees.",

        "DBMS":
            "Learn normalization and SQL.",

        "SQL":
            "Practice joins and queries.",

        "Operating Systems":
            "Study processes and scheduling.",

        "OOP Concepts":
            "Understand encapsulation and inheritance."
    },

    "Aptitude": {

        "Percentages":
            "Practice percentage calculations.",

        "Probability":
            "Study basic probability concepts.",

        "Time and Work":
            "Solve efficiency problems.",

        "Logical Reasoning":
            "Practice patterns and logic.",

        "Number Series":
            "Identify sequences."
    },

    "Communication Skills": {

        "Self Introduction":
            "Prepare 60–90 second introduction.",

        "Tell Me About Yourself":
            "Talk about education, skills and goals.",

        "Explain Final Year Project":
            "Describe objective and outcome.",

        "Strengths and Weaknesses":
            "Give honest and balanced answers.",

        "Group Discussion":
            "Speak clearly and listen actively.",

        "Resume Walkthrough":
            "Explain each point confidently.",

        "Why Should We Hire You":
            "Connect skills with company needs.",

        "Communication Confidence":
            "Practice concise speaking.",

        "HR Interview Practice":
            "Prepare common HR questions."
    }
}


completed = []


def select_category():

    print("\nChoose Category")

    print("1. ECE Core")
    print("2. Software")
    print("3. Aptitude")
    print("4. Communication Skills")

    option = input("Choice: ")

    mapping = {
        "1": "ECE Core",
        "2": "Software",
        "3": "Aptitude",
        "4": "Communication Skills"
    }

    return mapping.get(option)


while True:

    print("\n===== SMART INTERVIEW PREPARATION ASSISTANT =====")

    print("1. Study Topics")
    print("2. Mark Topic Done")
    print("3. View Progress")
    print("4. Ask Doubt")
    print("5. Exit")

    choice = input("\nEnter choice: ")

    if choice == "1":

        category = select_category()

        if category:

            print(f"\nTopics ({category})")

            for i, topic in enumerate(
                    topics[category],
                    start=1):

                mark = "✓" if topic in completed else ""

                print(f"{i}. {topic} {mark}")

    elif choice == "2":

        category = select_category()

        if category:

            names = list(
                topics[category].keys()
            )

            for i, t in enumerate(
                    names,
                    start=1):

                print(i, t)

            done = input(
                "\nEnter completed topic number: "
            )

            if done.isdigit():

                index = int(done) - 1

                if 0 <= index < len(names):

                    completed.append(
                        names[index]
                    )

                    print(
                        "Topic Completed ✓"
                    )

    elif choice == "3":

        print("\nYOUR PROGRESS")

        if completed:

            for item in completed:

                print("✓", item)

        else:

            print(
                "No completed topics"
            )

    elif choice == "4":

        category = select_category()

        if category:

            names = list(
                topics[category].keys()
            )

            for i, t in enumerate(
                    names,
                    start=1):

                print(i, t)

            ask = input(
                "\nEnter topic number: "
            )

            if ask.isdigit():

                index = int(ask) - 1

                if (
                    0 <= index
                    < len(names)
                ):

                    topic = names[index]

                    print(
                        "\nStudy Guidance:"
                    )

                    print(
                        topics[
                            category
                        ][topic]
                    )

    elif choice == "5":

        print(
            "\nGood luck for placements 🚀"
        )

        break

    else:

        print("Invalid choice")
