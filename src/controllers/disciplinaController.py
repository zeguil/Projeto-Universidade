from sqlalchemy.orm import Session
from fastapi import HTTPException
from  models.model import Disciplina
from schemas.disciplina import *
from schemas.nota import NotaCreate

class DisciplinaController:
    def __init__(self, db: Session):
        self.db = db

    def list_disciplinas(self):
        return self.db.query(Disciplina).all()

    def get_disciplina(self, disciplina_id: int):
        return self.db.query(Disciplina).filter(Disciplina.id == disciplina_id).first()

    def create_disciplina(self, disciplina: DisciplinaCreate):
        db_disciplina = Disciplina(**disciplina.dict())
        self.db.add(db_disciplina)
        self.db.commit()
        self.db.refresh(db_disciplina)
        return db_disciplina

    def update_disciplina(self, disciplina_id: int, disciplina: DisciplinaUpdate):
        db_disciplina = self.db.query(Disciplina).filter(Disciplina.id == disciplina_id).first()
        if not db_disciplina:
            raise HTTPException(status_code=404, detail="Disciplina not found")
        for key, value in disciplina.dict().items():
            setattr(db_disciplina, key, value)
        self.db.commit()
        self.db.refresh(db_disciplina)
        return db_disciplina

    def delete_disciplina(self, disciplina_id: int):
        db_disciplina = self.db.query(Disciplina).filter(Disciplina.id == disciplina_id).first()
        if not db_disciplina:
            raise HTTPException(status_code=404, detail="Disciplina not found")
        self.db.delete(db_disciplina)
        self.db.commit()
        return db_disciplina
