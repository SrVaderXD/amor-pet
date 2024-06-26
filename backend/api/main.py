import os
import sqlite3
from fastapi import FastAPI, Form, HTTPException, Request
from fastapi.responses import FileResponse, HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel

app = FastAPI()

# Diretórios relativos
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
STATIC_DIR = os.path.join(BASE_DIR, '../../frontend/static')
TEMPLATES_DIR = os.path.join(BASE_DIR, '../../frontend/templates')
DB_PATH = os.path.join(BASE_DIR, '../../backend/banco_pets/banco_pets.db')

# Montar arquivos estáticos
app.mount("/static", StaticFiles(directory=STATIC_DIR), name="static")

# Configurar templates
templates = Jinja2Templates(directory=TEMPLATES_DIR)

# Conecta com o banco
def connection_to_database():
    try:
        connection = sqlite3.connect(DB_PATH)
        cursor = connection.cursor()
        print("Conexão com o banco de dados estabelecida com sucesso!")
        return connection, cursor
    except sqlite3.Error as e:
        print(f"Erro ao conectar ao banco de dados: {e}")
        return None, None

# Modelo para os dados da consulta
class Consulta(BaseModel):
    nome_pet: str
    data_consulta: str
    veterinario: str

# Queries
def query_get_all_data(cursor):
    try:
        cursor.execute("SELECT * FROM consultas_pet")
        pets = cursor.fetchall()
        return pets
    except sqlite3.Error as e:
        print(f"Erro ao obter os dados dos pets: {e}")
        return pets

def query_insert_data(cursor, connection, consulta: Consulta):
    try:
        cursor.execute("INSERT INTO consultas_pet (nome_pet, data_consulta, veterinario) VALUES (?, ?, ?)",
                       (consulta.nome_pet, consulta.data_consulta, consulta.veterinario))
        connection.commit()
    except sqlite3.Error as e:
        print(f"Erro ao inserir os dados da consulta: {e}")
        raise HTTPException(status_code=500, detail="Erro ao inserir os dados da consulta")
    
def search_query(cursor, searched_word):
    try:
        cursor.execute(f"""
                    SELECT 
                    * 
                    FROM consultas_pet
                    WHERE
                    veterinario LIKE '%{searched_word}%'""")
        consulta = cursor.fetchall()
        return consulta
    except sqlite3.Error as e:
        print(f"Erro ao obter os dados dos pets: {e}")
        return consulta

# Rotas
@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    with open("../../frontend/templates/index.html", encoding="utf-8") as f:
        return templates.TemplateResponse("index.html", {"request": request})

@app.get("/pesquisar-consulta/", response_class=HTMLResponse)
async def cadastrar_consulta(request: Request):
    with open("../../frontend/templates/pesquisarconsul.html", encoding="utf-8") as f:
        return templates.TemplateResponse("pesquisarconsul.html", {"request": request})

@app.get("/ver-consulta")
async def get_consultas(palavra: str = ''):
    connection_db, cursor = connection_to_database()
    pets = search_query(cursor, palavra)
    connection_db.close()
    return {"data": pets}

@app.get("/area-do-vet/")
async def area_do_vet(request: Request):
    with open("../../frontend/templates/areadovet.html", encoding="utf-8") as f:
        return templates.TemplateResponse("areadovet.html", {"request": request})
    
@app.get("/areadovet-logged/", response_class=HTMLResponse)
async def intermediate(request: Request):
    return templates.TemplateResponse("areadovetlogged.html", {"request": request})

@app.get("/cadastrar-consulta/", response_class=HTMLResponse)
async def cadastrar_consulta(request: Request):
    with open("../../frontend/templates/regconsultas.html", encoding="utf-8") as f:
        return templates.TemplateResponse("regconsultas.html", {"request": request})

@app.post("/cadastrar-consulta/", response_class=HTMLResponse)
async def cadastrar_consulta(request: Request, nome_pet: str = Form(...), data_consulta: str = Form(...), veterinario: str = Form(...)):
    with open("../../frontend/templates/regconsultas.html", encoding="utf-8") as f:
        consulta = Consulta(nome_pet=nome_pet, data_consulta=data_consulta, veterinario=veterinario)
        connection_db, cursor = connection_to_database()
        if connection_db is None:
            raise HTTPException(status_code=500, detail="Erro ao conectar ao banco de dados")
        query_insert_data(cursor, connection_db, consulta)
        connection_db.close()
        return templates.TemplateResponse("regconsultas.html", {"request": request, "message": "Consulta cadastrada com sucesso!"})

@app.get("/contato/", response_class=HTMLResponse)
async def contato(request: Request):
    with open("../../frontend/templates/contato.html", encoding="utf-8") as f:
        return templates.TemplateResponse("contato.html", {"request": request})
    
@app.get("/favicon.ico", include_in_schema=False)
async def favicon():
    return FileResponse(os.path.join(STATIC_DIR, "favicon.ico"))