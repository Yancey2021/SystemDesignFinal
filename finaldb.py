import sqlite3
conn = sqlite3.connect("BradfordHotel.db")

print("Database connected.")

cmd = "CREATE TABLE Reservation (name TEXT, CheckInDate TEXT, CheckOutDate TEXT, RoomType TEXT)"

conn.execute(cmd)

print("Table created successfully.")

conn.close()