import os
import sqlite3

# Caminho do banco de dados
folder_path = '/home/henriqueic/personal-projects/pi/backend/banco_pets/'
db_name = 'banco_pets.db'
db_path = os.path.join(folder_path, db_name)

# Conecta ao banco de dados
connection = sqlite3.connect(db_path)
cursor = connection.cursor()

# Cria a tabela consultas_pet
cursor.execute (
'''CREATE TABLE IF NOT EXISTS consultas_pet (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome_pet TEXT,
        data_consulta TEXT,
        veterinario TEXT
    )'''
)

# Commit e fecha a conexão
connection.commit()
connection.close()