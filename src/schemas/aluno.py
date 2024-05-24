from pydantic import BaseModel
from typing import Optional
from datetime import date

class AlunoBase(BaseModel):
    id: int
    nome: str
    data_nascimento: date
    email: str

    class Config:
        orm_mode = True

class AlunoCreate(BaseModel):
    nome: str
    data_nascimento: str
    email: str

class AlunoUpdate(BaseModel):
    nome: Optional[str] = None
    data_nascimento: Optional[str] = None
    email: Optional[str] = None
