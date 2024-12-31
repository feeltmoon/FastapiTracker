# backend/main.py
from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from .database import engine, get_db
from .models import Base, Information

Base.metadata.create_all(bind=engine)

app = FastAPI()

@app.post("/submit_info")
def submit_info(lead_dbp: str, study: str, email: str, study_status: str, db: Session = Depends(get_db)):
    """
    Existing endpoint to receive 4 input fields and store them in the database.
    """
    info = Information(
        lead_dbp=lead_dbp,
        study=study,
        email=email,
        study_status=study_status
    )
    db.add(info)
    db.commit()
    db.refresh(info)
    return {"message": "Information has been saved. Thanks."}


@app.get("/get_info")
def get_info(db: Session = Depends(get_db)):
    """
    New endpoint to retrieve all records from the `information` table.
    Returns a list of dictionaries with all data in JSON.
    """
    results = db.query(Information).all()

    # Convert each database row to a dictionary
    data = []
    for r in results:
        data.append({
            "id": r.id,
            "lead_dbp": r.lead_dbp,
            "study": r.study,
            "email": r.email,
            "study_status": r.study_status
        })

    return data
