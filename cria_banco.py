import sqlite3


connection = sqlite3.connect('banco.db')
cursor = connection.cursor()


cria_tabela = "CREATE TABLE IF NOT EXISTS hoteis (hotel_id text PRIMARY KEY, nome text, endereco text)"
cria_hotel = "INSERT INTO hoteis VALUES ('1', 'Hotel da Silva', 'Rua dos Bobos, 1000')"

cursor.execute(cria_tabela)
cursor.execute(cria_hotel)


connection.commit()
connection.close()