from sqlalchemy.orm import Session
from fastapi import HTTPException
from models.model import Nota
from schemas.nota import NotaBase, NotaCreate, NotaUpdate
from typing import List
from datetime import datetime, timezone, timedelta

class NotaController:
    def __init__(self, db: Session):
        self.db = db

    def list_notas(self) -> List[NotaBase]:
        return self.db.query(Nota).all()

    def create_n1(self, nota: NotaCreate) -> NotaBase:
        if nota.n2 is not None:
            raise HTTPException(status_code=400, detail="N2 should not be provided when creating N1.")
        db_nota = Nota(
            aluno_id=nota.aluno_id,
            disciplina_id=nota.disciplina_id,
            n1=nota.n1,
            data_nota=datetime.now(timezone.utc) - timedelta(hours=4)
        )
        self.db.add(db_nota)
        self.db.commit()
        self.db.refresh(db_nota)
        return db_nota

    def create_n2(self, aluno_id: int, disciplina_id: int, n2: float) -> NotaBase:
        db_nota = self.db.query(Nota).filter(
            Nota.aluno_id == aluno_id,
            Nota.disciplina_id == disciplina_id
        ).first()
        if not db_nota:
            raise HTTPException(status_code=404, detail="Nota not found for the given aluno and disciplina.")
        if db_nota.n1 is None:
            raise HTTPException(status_code=400, detail="N1 must be provided before N2.")

        db_nota.n2 = n2
        db_nota.media = (db_nota.n1 + db_nota.n2) / 2
        self.db.commit()
        self.db.refresh(db_nota)
        return db_nota

    def update_nota(self, nota_id: int, nota: NotaUpdate) -> NotaBase:
        db_nota = self.db.query(Nota).filter(Nota.id == nota_id).first()
        if not db_nota:
            raise HTTPException(status_code=404, detail="Nota not found")

        if nota.n1 is not None:
            db_nota.n1 = nota.n1
        if nota.n2 is not None:
            db_nota.n2 = nota.n2
            db_nota.media = (db_nota.n1 + db_nota.n2) / 2

        self.db.commit()
        self.db.refresh(db_nota)
        return db_nota

    def delete_nota(self, nota_id: int) -> NotaBase:
        db_nota = self.db.query(Nota).filter(Nota.id == nota_id).first()
        if not db_nota:
            raise HTTPException(status_code=404, detail="Nota not found")

        self.db.delete(db_nota)
        self.db.commit()
        return db_nota
