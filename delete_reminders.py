import sqlite3

def delete_reminders():
    conn = sqlite3.connect("database.sqlite")
    cursor = conn.cursor()

    print("Do you want to delete (1) All reminders or (2) Specific ID?")
    choice = input("Enter 1 or 2: ")

    if choice == "1":
        cursor.execute("DELETE FROM reminders")
        print("All reminders deleted successfully.")
    elif choice == "2":
        reminder_id = input("Enter the Reminder ID to delete: ")
        cursor.execute("DELETE FROM reminders WHERE id=?", (reminder_id,))
        print(f"Reminder with ID {reminder_id} deleted successfully.")
    else:
        print("Invalid choice.")

    conn.commit()
    conn.close()

if __name__ == "__main__":
    delete_reminders()
