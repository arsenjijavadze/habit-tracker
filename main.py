import argparse
from tracker import add_habit, mark_habit, show_stats

def main() -> None:
    """Main function to handle CLI commands for the Habit Tracker."""
    parser = argparse.ArgumentParser(description="Habit Tracker CLI")
    parser.add_argument(
        "command",
        choices=["add", "mark", "stats"],
        help="Command to run (e.g., add, mark, stats)"
    ) 
    parser.add_argument(
        "name",
        nargs="*",
        help="Name of the habit (required for the 'add' command)"
    )
    args: argparse.Namespace = parser.parse_args()

    if args.command == "add":
        habit_name = " ".join(args.name).strip()
        if habit_name:
            add_habit(habit_name)
        else: 
            print("Error: Please provide a habit name to add.")
    elif args.command == "mark":
        mark_habit()
    elif args.command == "stats":
        show_stats()
    else: 
        print("Unknown command. Use 'add', 'mark', or 'stats'.")


if __name__ == "__main__":
    main()


