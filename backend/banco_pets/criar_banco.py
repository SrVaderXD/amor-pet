import os
import sqlite3

# Verifica se a pasta existe e criar se não existir
folder_path = '/home/henriqueic/personal-projects/pi/backend/banco_pets/'
if not os.path.exists(folder_path):
    os.makedirs(folder_path)

# Caminho do banco de dados
db_name = 'banco_pets.db'
db_path = os.path.join(folder_path, db_name)

# Conecta e desconecta o banco de dados
connection = sqlite3.connect(db_path)
connection.close()