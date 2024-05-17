from pydantic import BaseModel
from datetime import date
from typing import Optional

class AlunoBase(BaseModel):
    nome: str
    data_nascimento: date
    email: str

class AlunoCreate(AlunoBase):
    pass

class AlunoUpdate(AlunoBase):
    pass


