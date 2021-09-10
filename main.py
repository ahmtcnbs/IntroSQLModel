from typing import Optional
from fastapi import FastAPI, Form
from sqlmodel import Field, Session, SQLModel, create_engine
import uvicorn

app = FastAPI(version="1.0.0", title="Introduction to SQLModel", description="Author: Ahmet BAŞ")

class train(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    fullname: str
    age: int
    gender: str

@app.post("/writetodb", description="Write to Database")
async def write_to_db(fullname : str = Form(...), age : int = Form(...), gender : str = Form(...)):

    adding_data = train(fullname=fullname, age=age, gender=gender)

    engine = create_engine("sqlite:///sqlmodel.db")

    SQLModel.metadata.create_all(engine)

    with Session(engine) as session:
        session.add(adding_data)
        session.commit()

if __name__ == '__main__':
    uvicorn.run(app, port=5959, host='0.0.0.0')