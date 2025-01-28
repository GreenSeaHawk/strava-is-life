from connection import connect_to_db, close_db_connection
import json


def seed():
    conn = connect_to_db()

    try:
        conn.run("DROP TABLE IF EXISTS activities;")
        conn.run(
            "CREATE TABLE activities (\
                activity_id SERIAL PRIMARY KEY,\
                name TEXT,\
                distance FLOAT,\
                moving_time INTEGER,\
                elapsed_time INTEGER,\
                type TEXT,\
                sport_type TEXT,\
                location_country TEXT,\
                kudos_count INTEGER,\
                suffer_score FLOAT,\
                date TIMESTAMP\
            );"
        )
        activities_path = "db/activities.json"
        with open(activities_path, "r") as file:
            data = json.load(file)
        count = 0
        for activity in data:
            count += 1
            # print(count, activity["name"])
            conn.run(
                """INSERT INTO activities (name, distance, moving_time, elapsed_time, type, sport_type,
                  location_country, kudos_count, suffer_score, date) 
                VALUES (:name, :distance, :moving_time, :elapsed_time, :type, :sport_type,
                  :location_country, :kudos_count, :suffer_score, :date)""",
                name = activity["name"],
                distance = activity["distance"],
                moving_time = activity["moving_time"],
                elapsed_time = activity["elapsed_time"],
                type = activity["type"],
                sport_type = activity["sport_type"],
                location_country = activity["location_country"],
                kudos_count = activity["kudos_count"],
                suffer_score = activity.get("suffer_score"),
                date = activity["start_date_local"]
            )

    finally:
        print("Seeding Complete.")
        close_db_connection(conn)

seed()
