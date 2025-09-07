# # Placeholder for Scheduler Agent implementation
# import sqlite3
# from datetime import datetime

# class SchedulerAgent:
#     def __init__(self, db_path='database.sqlite'):
#         self.db_path = db_path
#         self._initialize_db()

#     def _initialize_db(self):
#         conn = sqlite3.connect(self.db_path)
#         cursor = conn.cursor()
#         cursor.execute('''
#             CREATE TABLE IF NOT EXISTS reminders (
#                 id INTEGER PRIMARY KEY AUTOINCREMENT,
#                 symptom TEXT,
#                 advice TEXT,
#                 reminder_time TEXT
#             )
#         ''')
#         conn.commit()
#         conn.close()

#     def schedule_reminder(self, symptom, advice):
#         reminder_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
#         conn = sqlite3.connect(self.db_path)
#         cursor = conn.cursor()
#         cursor.execute('''
#             INSERT INTO reminders (symptom, advice, reminder_time)
#             VALUES (?, ?, ?)
#         ''', (symptom, advice, reminder_time))
#         conn.commit()
#         conn.close()

#         return {'reminder': f"Reminder set for '{symptom}' advice.", 'status': 'success'}


import sqlite3
from datetime import datetime, timedelta

class SchedulerAgent:
    def __init__(self):
        self.conn = sqlite3.connect("database.sqlite", check_same_thread=False)
        self.cursor = self.conn.cursor()
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS reminders (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                symptom TEXT,
                advice TEXT,
                reminder_time TEXT
            )
        ''')
        self.conn.commit()

    def set_reminders(self, symptoms, advice_list):
        reminders = []
        for symptom, advice in zip(symptoms, advice_list):
            reminder_time = (datetime.now() + timedelta(hours=6)).strftime('%Y-%m-%d %H:%M:%S')
            self.cursor.execute('''
                INSERT INTO reminders (symptom, advice, reminder_time)
                VALUES (?, ?, ?)
            ''', (symptom, advice['advice']))
            self.conn.commit()
            reminders.append({
                "symptom": symptom,
                "advice": advice['advice'],
                "reminder_time": reminder_time
            })
        return {"reminders": reminders}
