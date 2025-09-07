import sqlite3

def check_reminders():
    conn = sqlite3.connect("database.sqlite")
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM reminders")
    rows = cursor.fetchall()

    if rows:
        print("\n⏰ Current Reminders:")
        for row in rows:
            print(f"ID: {row[0]}, Symptom: {row[1]}, Advice: {row[2]}, Reminder Time: {row[3]}")
    else:
        print("\nNo reminders found.")

    conn.close()

if __name__ == "__main__":
    check_reminders()
