import argparse
from tracker import add_habit, mark_habit, show_stats

def main() -> None:
    """Main function to handle CLI commands for the Habit Tracker."""
    parser = argparse.ArgumentParser(description="Habit Tracker CLI")
    parser.add_argument("command", type=str, help="Command to run (e.g., add, mark, stats)")
    args: argparse.Namespace = parser.parse_args()

    if args.command == "add":
        add_habit()
    elif args.command == "mark":
        mark_habit()
    elif args.command == "stats":
        show_stats()
    else: 
        print("Unknown command. Use 'add', 'mark', or 'stats'.")


if __name__ == "__main__":
    main()


