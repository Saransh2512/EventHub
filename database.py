
import sqlite3


def create_database():
    connection = sqlite3.connect("eventhub.db")

    cursor = connection.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS events (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            description TEXT NOT NULL,
            event_date TEXT,
            venue TEXT,
            organizer TEXT,
            category TEXT
        )
    """)

    connection.commit()
    connection.close()


def insert_sample_events():
    connection = sqlite3.connect("eventhub.db")
    cursor = connection.cursor()

    sample_events = [
        (
            "Chitrakala",
            "A campus art and creativity event.",
            "2026-10-25",
            "Venue to be announced",
            "NSS",
            "Art & Culture"
        ),
        (
            "Blood Donation Camp",
            "A community initiative to support blood donation.",
            "2027-02-15",
            "MAC",
            "NSS",
            "Social Impact"
        ),
        (
            "Spandan",
            "A campus sports festival celebrating teamwork.",
            "2027-03-10",
            "Cricket Ground",
            "Sports Committee",
            "Sports"
        )
    ]

    cursor.executemany("""
        INSERT INTO events
        (name, description, event_date, venue, organizer, category)
        VALUES (?, ?, ?, ?, ?, ?)
    """, sample_events)

    connection.commit()
    connection.close()

    print("Sample events inserted successfully!")



if __name__ == "__main__":
    create_database()
    insert_sample_events()
    print("EventHub database setup completed!")
