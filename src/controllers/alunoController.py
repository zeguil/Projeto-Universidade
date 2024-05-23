from sqlalchemy.orm import Session
from fastapi import HTTPException
from models.model import Aluno
from schemas.aluno import AlunoBase, AlunoCreate, AlunoUpdate
from typing import List

class AlunoController:
    def __init__(self, db: Session):
        self.db = db

    def listar_alunos(self) -> List[AlunoBase]:
        return self.db.query(Aluno).all()

    def criar_aluno(self, aluno: AlunoCreate) -> AlunoBase:
        db_aluno = Aluno(
            nome=aluno.nome,
            data_nascimento=aluno.data_nascimento,
            email=aluno.email
        )
        self.db.add(db_aluno)
        self.db.commit()
        self.db.refresh(db_aluno)
        return db_aluno

    def atualizar_aluno(self, aluno_id: int, aluno: AlunoUpdate) -> AlunoBase:
        db_aluno = self.db.query(Aluno).filter(Aluno.id == aluno_id).first()
        if not db_aluno:
            raise HTTPException(status_code=404, detail="Aluno não encontrado")

        if aluno.nome is not None:
            db_aluno.nome = aluno.nome
        if aluno.data_nascimento is not None:
            db_aluno.data_nascimento = aluno.data_nascimento
        if aluno.email is not None:
            db_aluno.email = aluno.email

        self.db.commit()
        self.db.refresh(db_aluno)
        return db_aluno

    def deletar_aluno(self, aluno_id: int) -> AlunoBase:
        db_aluno = self.db.query(Aluno).filter(Aluno.id == aluno_id).first()
        if not db_aluno:
            raise HTTPException(status_code=404, detail="Aluno não encontrado")

        self.db.delete(db_aluno)
        self.db.commit()
        return db_aluno
