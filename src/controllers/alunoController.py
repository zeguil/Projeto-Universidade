from sqlalchemy.orm import Session
from fastapi import HTTPException
from  models.model import Aluno
from schemas.aluno import *
from schemas.nota import NotaCreate

class AlunoController:
    def __init__(self, db: Session):
        self.db = db

    def list_users(self):
        return self.db.query(Aluno).all()

    def get_nota(self, nota_id: int):
        return self.db.query(Aluno).filter(Aluno.id == nota_id).first()

    def create_nota(self, nota: NotaCreate):
        db_nota = Aluno(**nota.dict())
        self.db.add(db_nota)
        self.db.commit()
        self.db.refresh(db_nota)
        return db_nota

    def update_nota(self, nota_id: int, nota: AlunoUpdate):
        db_nota = self.db.query(Aluno).filter(Aluno.id == nota_id).first()
        if not db_nota:
            raise HTTPException(status_code=404, detail="Nota not found")
        for key, value in nota.dict().items():
            setattr(db_nota, key, value)
        self.db.commit()
        self.db.refresh(db_nota)
        return db_nota

    def delete_nota(self, nota_id: int):
        db_nota = self.db.query(Aluno).filter(Aluno.id == nota_id).first()
        if not db_nota:
            raise HTTPException(status_code=404, detail="Nota not found")
        self.db.delete(db_nota)
        self.db.commit()
        return db_nota
