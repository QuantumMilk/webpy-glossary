from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from app import models, schemas, database

app = FastAPI()

database.init_db()

def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/terms/", response_model=schemas.Term)
def create_term(term: schemas.TermCreate, db: Session = Depends(get_db)):
    db_term = db.query(models.Term).filter(models.Term.term == term.term).first()
    if db_term:
        raise HTTPException(status_code=400, detail="Term already exists")
    db_term = models.Term(**term.dict())
    db.add(db_term)
    db.commit()
    db.refresh(db_term)
    return db_term

@app.get("/terms/", response_model=list[schemas.Term])
def get_terms(db: Session = Depends(get_db)):
    return db.query(models.Term).all()

@app.get("/terms/{term_name}", response_model=schemas.Term)
def get_term(term_name: str, db: Session = Depends(get_db)):
    db_term = db.query(models.Term).filter(models.Term.term == term_name).first()
    if db_term is None:
        raise HTTPException(status_code=404, detail="Term not found")
    return db_term

@app.put("/terms/{term_name}", response_model=schemas.Term)
def update_term(term_name: str, term: schemas.TermUpdate, db: Session = Depends(get_db)):
    db_term = db.query(models.Term).filter(models.Term.term == term_name).first()
    if db_term is None:
        raise HTTPException(status_code=404, detail="Term not found")
    db_term.description = term.description
    db.commit()
    db.refresh(db_term)
    return db_term

@app.delete("/terms/{term_name}", response_model=schemas.Term)
def delete_term(term_name: str, db: Session = Depends(get_db)):
    db_term = db.query(models.Term).filter(models.Term.term == term_name).first()
    if db_term is None:
        raise HTTPException(status_code=404, detail="Term not found")
    db.delete(db_term)
    db.commit()
    return db_term