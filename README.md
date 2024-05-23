# Sistema Escolar - API com SQLAlchemy e FastAPI

## Introdução

Este projeto é uma API básica para gerenciamento de notas escolares, utilizando SQLAlchemy como ORM (Object Relational Mapper) para mapeamento objeto-relacional e FastAPI como framework para desenvolvimento da API.

## Modelos

Os modelos da API representam as entidades do sistema:

### Aluno

Atributos:
- **id:** Identificador único do aluno (chave primária).
- **nome:** Nome completo do aluno.
- **data_nascimento:** Data de nascimento do aluno no formato YYYY-MM-DD.
- **email:** Endereço de email do aluno (único).

### Disciplina

Atributos:
- **id:** Identificador único da disciplina (chave primária).
- **nome_disciplina:** Nome da disciplina.
- **professor_responsavel:** Nome do professor responsável pela disciplina.

### Nota

Atributos:
- **id:** Identificador único da nota (chave primária).
- **aluno_id:** Chave estrangeira para o aluno que recebeu a nota.
- **disciplina_id:** Chave estrangeira para a disciplina à qual a nota se refere.
- **n1:** Nota da primeira avaliação (opcional).
- **n2:** Nota da segunda avaliação (opcional).
- **media:** Média final da nota, calculada automaticamente a partir de n1 e n2 (se ambas estiverem presentes).
- **data_nota:** Data e hora da criação da nota, armazenada automaticamente no timezone UTC-4 (Manaus, Amazonas).

Observações:
- A relação entre Aluno e Nota é um para muitos, ou seja, um aluno pode ter várias notas.
- A relação entre Disciplina e Nota também é um para muitos, ou seja, uma disciplina pode ter várias notas.

## Controllers

Os controllers da API gerenciam as operações CRUD (Criar, Ler, Atualizar, Deletar) para cada modelo:

### AlunoController

- **listar_alunos():** Lista todos os alunos.
- **criar_aluno(aluno: AlunoCreate):** Cria um novo aluno.
- **atualizar_aluno(aluno_id: int, aluno: AlunoUpdate):** Atualiza um aluno existente.
- **deletar_aluno(aluno_id: int):** Deleta um aluno existente.

### DisciplinaController

- **listar_disciplinas():** Lista todas as disciplinas.
- **criar_disciplina(disciplina: DisciplinaCreate):** Cria uma nova disciplina.
- **atualizar_disciplina(disciplina_id: int, disciplina: DisciplinaUpdate):** Atualiza uma disciplina existente.
- **deletar_disciplina(disciplina_id: int):** Deleta uma disciplina existente.

### NotaController

- **listar_notas():** Lista todas as notas.
- **criar_n1(nota: NotaCreate):** Cria uma nova nota N1 para um aluno em uma disciplina específica.
- **criar_n2(aluno_id: int, disciplina_id: int, n2: float):** Cria uma nova nota N2 para um aluno em uma disciplina específica.
- **atualizar_nota(nota_id: int, nota: NotaUpdate):** Atualiza uma nota existente (n1, n2 ou ambos).
- **deletar_nota(nota_id: int):** Deleta uma nota existente.

Observações:
- A criação da nota N2 só é permitida após a N1 ter sido informada.
- A atualização da nota recalcula a média automaticamente.

## Executando o Projeto

### Pré-requisitos

- Python 3.8 ou superior
- SQLAlchemy
- FastAPI
- Banco de dados SQLite

### Etapas

1. **Instalar dependências:**

```bash
pip install -r requirements.txt
```


2. **Iniciar a API:**

```bash
uvicorn main:app --reload
```

**OU**

```bash
docker-compose up
```

3. **Acesse no Navegador:**


*http://localhost:8000*
