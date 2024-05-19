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
    ('Marley', '2024-05-06', 'Dr. Ferreira'),
    ('Lulu', '2024-05-07', 'Dr. Klebinho Machadão'),
    ('Max', '2024-05-08', 'Dr. Klebinho Machadão'),
    ('Bella', '2024-05-09', 'Dr. Klebinho Machadão'),
    ('Charlie', '2024-05-10', 'Dr. Klebinho Machadão'),
    ('Buddy', '2024-05-11', 'Dr. Klebinho Machadão'),
    ('Molly', '2024-05-12', 'Dr. Klebinho Machadão'),
    ('Lucy', '2024-05-13', 'Dr. Klebinho Machadão'),
    ('Daisy', '2024-05-14', 'Dr. Klebinho Machadão'),
    ('Bailey', '2024-05-15', 'Dr. Klebinho Machadão'),
    ('Lola', '2024-05-16', 'Dr. Klebinho Machadão'),
    ('Sadie', '2024-05-17', 'Dr. Klebinho Machadão'),
    ('Cooper', '2024-05-18', 'Dr. Klebinho Machadão'),
    ('Sophie', '2024-05-19', 'Dr. Klebinho Machadão'),
    ('Rosie', '2024-05-20', 'Dr. Klebinho Machadão'),
    ('Rocky', '2024-05-21', 'Dr. Klebinho Machadão'),
    ('Zoe', '2024-05-22', 'Dr. Santos'),
    ('Chloe', '2024-05-23', 'Dra. Oliveira'),
    ('Jack', '2024-05-24', 'Dr. Silva'),
    ('Toby', '2024-05-25', 'Dra. Souza'),
    ('Buster', '2024-05-26', 'Dr. Ferreira'),
    ('Lily', '2024-05-27', 'Dr. Santos'),
    ('Duke', '2024-05-28', 'Dra. Oliveira'),
    ('Gracie', '2024-05-29', 'Dr. Silva'),
    ('Stella', '2024-05-30', 'Dra. Souza'),
    ('Milo', '2024-05-31', 'Dr. Ferreira')
]
    
cursor.executemany(
    '''INSERT INTO consultas_pet (nome_pet, data_consulta, veterinario)
        VALUES (?, ?, ?)''', 
        dados
)

# Commit e fecha a conexão
connection.commit()
connection.close()