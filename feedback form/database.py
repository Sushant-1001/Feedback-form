import mysql.connector

# Database connection

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="feedback_db"
)

cursor = conn.cursor()