from sqlalchemy.orm import Session
from fastapi import HTTPException
from models import Nota
from schemas import NotaCreate, NotaUpdate
from datetime import datetime, timezone, timedelta

class NotaController:
    def __init__(self, db: Session):
        self.db = db

    def list_notas(self):
        return self.db.query(Nota).all()

    def get_nota(self, nota_id: int):
        return self.db.query(Nota).filter(Nota.id == nota_id).first()

    def create_nota(self, nota: NotaCreate):
        db_nota = Nota(**nota.dict(exclude={"media"}))

        if nota.n1 is None:
            raise HTTPException(status_code=400, detail="N1 must be provided.")

        if nota.n2 is not None and db_nota.n1 is None:
            raise HTTPException(status_code=400, detail="N1 must be provided before N2.")

        if nota.n2 is not None:
            db_nota.media = (nota.n1 + nota.n2) / 2

        db_nota.data_nota = datetime.now(timezone.utc) - timedelta(hours=4)

        self.db.add(db_nota)
        self.db.commit()
        self.db.refresh(db_nota)
        return db_nota

    def update_nota(self, nota_id: int, nota: NotaUpdate):
        db_nota = self.db.query(Nota).filter(Nota.id == nota_id).first()
        if not db_nota:
            raise HTTPException(status_code=404, detail="Nota not found")

        for key, value in nota.dict(exclude={"media"}).items():
            setattr(db_nota, key, value)

        if db_nota.n1 is not None and db_nota.n2 is not None:
            db_nota.media = (db_nota.n1 + db_nota.n2) / 2

        self.db.commit()
        self.db.refresh(db_nota)
        return db_nota

    def delete_nota(self, nota_id: int):
        db_nota = self.db.query(Nota).filter(Nota.id == nota_id).first()
        if not db_nota:
            raise HTTPException(status_code=404, detail="Nota not found")
        self.db.delete(db_nota)
        self.db.commit()
        return db_nota
