import argparse


def main():
    parser = argparse.ArgumentParser(description="Habit Tracker CLI")
    parser.add_argument("command", help="Command to run (e.g., add, mark, stats)")
    args = parser.parse_args()

    if args.command == "add":
        print("Add a new habit")
    elif args.command == "mark":
        print("Mark a habit as done")
    elif args.command == "stats":
        print("Show habit statistics")
    else:
        print("Unknown command. Use add, mark, or stats.")


if __name__ == "__main__":
    main()
