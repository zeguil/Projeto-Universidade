from sqlalchemy import Column, Integer, String, Date, ForeignKey, Float, Date
from sqlalchemy.orm import relationship
from ..database import Base
from datetime import datetime, timezone
from zoneinfo import ZoneInfo

from database.config import Base

def get_current_time_utc_minus_4():
    return datetime.now(timezone.utc).astimezone(ZoneInfo("America/Manaus"))


class Aluno(Base):
    __tablename__ = "alunos"

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String, index=True)
    data_nascimento = Column(Date)
    email = Column(String, unique=True, index=True)
    

class Disciplina(Base):
    __tablename__ = "disciplinas"

    id = Column(Integer, primary_key=True, index=True)
    nome_disciplina = Column(String, index=True)
    professor_responsavel = Column(String)


class Nota(Base):
    __tablename__ = "notas"

    id = Column(Integer, primary_key=True, index=True)
    aluno_id = Column(Integer, ForeignKey("alunos.id"), nullable=False)
    disciplina_id = Column(Integer, ForeignKey("disciplinas.id"), nullable=False)
    n1 = Column(Float, nullable=False)
    n2 = Column(Float, nullable=True)
    media = Column(Float, nullable=True)
    data_nota = Column(Date, default=get_current_time_utc_minus_4)

    aluno = relationship("Aluno")
    disciplina = relationship("Disciplina")

    def calculate_media(self):
        if self.n1 is not None and self.n2 is not None:
            self.media = (self.n1 + self.n2) / 2