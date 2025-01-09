import argparse
from tracker import add_habit, mark_habit, show_stats

def main():
    parser = argparse.ArgumentParser(description="Habit Tracker CLI")
    parser.add_argument("command", help="Command to run (add, mark, stats)")
    args = parser.parse_args()

    try:
        if args.command == "add":
            add_habit()
        elif args.command == "mark":
            mark_habit()
        elif args.command == "stats":
            show_stats()
        else: 
            print("Unknown command. Use 'add', 'mark', or 'stats'.")
    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()


