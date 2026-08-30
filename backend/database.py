import sqlite3
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent
DATABASE_PATH = BASE_DIR / "website_monitor.db"


def get_connection():
    """Create and return a database connection."""
    return sqlite3.connect(DATABASE_PATH)


def initialize_database():
    """Create database tables if they do not already exist."""

    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS websites (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            url TEXT NOT NULL UNIQUE,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS monitoring_results (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            website_id INTEGER NOT NULL,
            status TEXT NOT NULL,
            status_code INTEGER,
            response_time REAL,
            checked_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY (website_id) REFERENCES websites(id)
        )
    """)

    connection.commit()
    connection.close()


def add_website(url):
    """Add a website to the database."""

    connection = get_connection()
    cursor = connection.cursor()

    try:
        cursor.execute(
            "INSERT INTO websites (url) VALUES (?)",
            (url,)
        )

        connection.commit()

        website_id = cursor.lastrowid

        return {
            "id": website_id,
            "url": url
        }

    except sqlite3.IntegrityError:
        return None

    finally:
        connection.close()


def get_websites():
    """Return all monitored websites."""

    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("""
        SELECT id, url, created_at
        FROM websites
        ORDER BY id DESC
    """)

    websites = cursor.fetchall()

    connection.close()

    return [
        {
            "id": website[0],
            "url": website[1],
            "created_at": website[2]
        }
        for website in websites
    ]


def save_monitoring_result(
    website_id,
    status,
    status_code,
    response_time
):
    """Save a monitoring result."""

    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("""
        INSERT INTO monitoring_results
        (
            website_id,
            status,
            status_code,
            response_time
        )
        VALUES (?, ?, ?, ?)
    """, (
        website_id,
        status,
        status_code,
        response_time
    ))

    connection.commit()
    connection.close()


def get_latest_result(website_id):
    """Get the latest monitoring result."""

    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("""
        SELECT
            status,
            status_code,
            response_time,
            checked_at
        FROM monitoring_results
        WHERE website_id = ?
        ORDER BY id DESC
        LIMIT 1
    """, (website_id,))

    result = cursor.fetchone()

    connection.close()

    if result is None:
        return None

    return {
        "status": result[0],
        "status_code": result[1],
        "response_time": result[2],
        "checked_at": result[3]
    }


if __name__ == "__main__":
    initialize_database()
    print("Database initialized successfully.")