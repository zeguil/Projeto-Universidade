from sqlalchemy.orm import Session
from fastapi import HTTPException
from models import Nota
from schemas import NotaCreateN1, NotaCreateN2
from datetime import datetime, timezone, timedelta

class NotaController:
    def __init__(self, db: Session):
        self.db = db

    def list_notas(self):
        return self.db.query(Nota).all()

    def get_nota(self, nota_id: int):
        return self.db.query(Nota).filter(Nota.id == nota_id).first()

    def create_n1(self, nota: NotaCreateN1):
        if nota.n1 is None:
            raise HTTPException(status_code=400, detail="N1 must be provided.")
        
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

    def create_n2(self, nota: NotaCreateN2):
        db_nota = self.db.query(Nota).filter(
            Nota.aluno_id == nota.aluno_id,
            Nota.disciplina_id == nota.disciplina_id
        ).first()
        
        if not db_nota:
            raise HTTPException(status_code=404, detail="N1 must be created before N2.")

        if db_nota.n1 is None:
            raise HTTPException(status_code=400, detail="N1 must be created before N2.")

        db_nota.n2 = nota.n2
        db_nota.media = (db_nota.n1 + db_nota.n2) / 2
        db_nota.data_nota = datetime.now(timezone.utc) - timedelta(hours=4)

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
