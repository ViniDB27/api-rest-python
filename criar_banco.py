import sqlite3

connection = sqlite3.connect('banco.db')
cursor = connection.cursor()

create_table = "CREATE TABLE IF NOT EXISTS hoteis (hotel_id text PRIMARY_KEY, name text, estrelas real, diaria real)"
create_hotel = "INSERT INTO hoteis VALUES ('alpha','Alpha Hotel',4.3,159.99)"


cursor.execute(create_table)
cursor.execute(create_hotel)

connection.commit()
connection.close()