import json
from datetime import datetime 
from typing import Any

DATA_FILE = "data.json"


def load_data() -> list[dict[str, Any]]:
    """Load habit data from the JSON file."""
    try:
        with open(DATA_FILE, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return [] 
    except json.JSONDecodeError:
        print("Error: Corrupted data file. Starting with an empty list.")
        return []


def save_data(data: list[dict[str, Any]]) -> None:
    """Save habit data to the JSON file."""
    with open(DATA_FILE, "w") as file:
        json.dump(data, file, indent=4)

def add_habit() -> None:
    """Add a new habit to the tracker."""
    habit_name = input("Enter the name of the new habit: ").strip()

    if not habit_name:
        print("Error: Habit name cannot be empty.")
        return 

    current_time = datetime.now().isoformat() # Get current date and time in ISO format

    new_habit = {
        "name": habit_name,
        "created_at": current_time, 
        "completed_dates": [] # Initialize with an empty list of completed dates
    }


    data = load_data() # Load existing habits 
    data.append(new_habit) # Add the new habit
    save_data(data) # Save the updated data

    print(f"Habit '{habit_name}' added successfully!")

def mark_habit() -> None:
    """Mark a habit as completed (under construction)."""
    print("Feature to mark a habit as done is under construction.")


def show_stats() -> None:
    """Show statistics for tracked habits (under construction)."""
    print("Feature to show habit statistics is under construction.")


