import argparse


def add_habit() -> None:
    """Add a new habit to the tracker."""
    print("Feature to add a new habit is under construction.")


def mark_habit() -> None:
    """Mark a habit as completed."""
    print("Feature to mark a habit as done is under construction.")


def show_stats() -> None:
    """Show statistics for tracked habits."""
    print("Feature to show habit statistics is under construction.")


def main() -> None:
    """Main entry point for the Habit Tracker CLI."""
    parser = argparse.ArgumentParser(description="Habit Tracker CLI")
    parser.add_argument("command", help="Command to run (e.g., add, mark, stats)")
    args = parser.parse_args()


    command = args.command.lower()
   

    try:
        if command == "add":
            add_habit()
        elif command == "mark":
            mark_habit()
        elif command == "stats":
            show_stats()
        else:
            print(f"Unknown command: {command}. Use 'add', 'mark', or 'stats'. ")
    except Exception as e:
        print(f"An error occured: {e}")


if __name__ == "__main__":
    main()
