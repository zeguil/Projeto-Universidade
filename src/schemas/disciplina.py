from pydantic import BaseModel
from typing import Optional

class DisciplinaBase(BaseModel):
    nome_disciplina: str
    professor_responsavel: str

class DisciplinaCreate(DisciplinaBase):
    pass

class DisciplinaUpdate(DisciplinaBase):
    pass


