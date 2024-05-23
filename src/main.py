import uvicorn
from typing import Dict
from models.model import *
from database.config import Base, engine
from routers.aluno import alunoRouter
from routers.disciplina import disciplinaRouter
from routers.nota import notaRouter
from sqlalchemy import inspect
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware


inspector = inspect(engine)

# Verificar se as tabelas já existem no banco de dados
existing_tables = inspector.get_table_names()

# Cria as tabelas se elas não existirem
if not existing_tables:
    Base.metadata.create_all(bind=engine)

app = FastAPI()

origins = [
    "http://localhost",
    "http://localhost:8080",
    "http://localhost:5173",
    "http://127.0.0.1",
    "http://127.0.0.1:5500",
    "http://127.0.0.1:5173/"
]

# Configuração CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(alunoRouter)
app.include_router(disciplinaRouter)
app.include_router(notaRouter)

@app.get("/")
def index() -> Dict:
    return {"acesse:": "localhost:8080/docs"}

if __name__ == "__main__":
    uvicorn.run(app, port=8080, host="localhost")