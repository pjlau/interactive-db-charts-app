import sqlite3

def get_sqlite_data():
    conn = sqlite3.connect("data/charts.db")
    cursor = conn.cursor()
    cursor.execute("SELECT date, value FROM line_chart_data")
    data = [{"date": row[0], "value": row[1]} for row in cursor.fetchall()]
    conn.close()
    return data