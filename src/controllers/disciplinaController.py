from sqlalchemy.orm import Session
from fastapi import HTTPException
from models.model import Disciplina
from schemas.disciplina import DisciplinaBase, DisciplinaCreate, DisciplinaUpdate
from typing import List

class DisciplinaController:
    def __init__(self, db: Session):
        self.db = db

    def list_disciplinas(self) -> List[DisciplinaBase]:
        return self.db.query(Disciplina).all()

    def create_disciplina(self, disciplina: DisciplinaCreate) -> DisciplinaBase:
        db_disciplina = Disciplina(
            nome_disciplina=disciplina.nome_disciplina,
            professor_responsavel=disciplina.professor_responsavel
        )
        self.db.add(db_disciplina)
        self.db.commit()
        self.db.refresh(db_disciplina)
        return db_disciplina

    def update_disciplina(self, disciplina_id: int, disciplina: DisciplinaUpdate) -> DisciplinaBase:
        db_disciplina = self.db.query(Disciplina).filter(Disciplina.id == disciplina_id).first()
        if not db_disciplina:
            raise HTTPException(status_code=404, detail="Disciplina not found")

        if disciplina.nome_disciplina is not None:
            db_disciplina.nome_disciplina = disciplina.nome_disciplina
        if disciplina.professor_responsavel is not None:
            db_disciplina.professor_responsavel = disciplina.professor_responsavel

        self.db.commit()
        self.db.refresh(db_disciplina)
        return db_disciplina

    def delete_disciplina(self, disciplina_id: int) -> DisciplinaBase:
        db_disciplina = self.db.query(Disciplina).filter(Disciplina.id == disciplina_id).first()
        if not db_disciplina:
            raise HTTPException(status_code=404, detail="Disciplina not found")

        self.db.delete(db_disciplina)
        self.db.commit()
        return db_disciplina
