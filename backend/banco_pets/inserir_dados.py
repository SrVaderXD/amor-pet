import os
import sqlite3

# Caminho do banco de dados
folder_path = '/home/henriqueic/personal-projects/pi/backend/banco_pets/'
db_name = 'banco_pets.db'
db_path = os.path.join(folder_path, db_name)

# Conecta ao banco de dados
connection = sqlite3.connect(db_path)
cursor = connection.cursor()

# Insere dados na tabela consultas_pet
dados = [
    ('Bolinha', '2024-05-02', 'Dr. Santos'),
    ('Frajola', '2024-05-03', 'Dra. Oliveira'),
    ('Rex', '2024-05-04', 'Dr. Silva'),
    ('Branquinho', '2024-05-05', 'Dra. Souza'),
    ('Marley', '2024-05-06', 'Dr. Ferreira')
]
    
cursor.executemany(
    '''INSERT INTO consultas_pet (nome_pet, data_consulta, veterinario)
        VALUES (?, ?, ?)''', 
        dados
)

# Commit e fecha a conexão
connection.commit()
connection.close()