from pydantic import BaseModel
from typing import Optional

class DisciplinaBase(BaseModel):
    id: int
    nome_disciplina: str
    professor_responsavel: str

    class Config:
        orm_mode = True

class DisciplinaCreate(BaseModel):
    nome_disciplina: str
    professor_responsavel: str

class DisciplinaUpdate(BaseModel):
    nome_disciplina: Optional[str] = None
    professor_responsavel: Optional[str] = None
