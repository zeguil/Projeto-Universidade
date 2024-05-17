from typing import List
from schemas.user import *
from config.database import Session
from fastapi import APIRouter, Depends
from config.dependencies import get_db
from controllers.userController import UserController
from utils.auth import logged_user

alunoRouter = APIRouter(prefix='/aluno', tags=['Aluno'] )

# Listar Usuários
@alunoRouter.get("/", response_model=List[AlunoResponse], status_code=200)
def list_users(db: Session = Depends(get_db)) -> List[AlunoResponse]:
    users = UserController(db).list_users()
    return users