from pydantic import BaseModel

class TermBase(BaseModel):
    term: str
    description: str


class TermCreate(TermBase):
    ...

class TermUpdate(TermBase):
    ...

class Term(TermBase):
    id: int

    class Config:
        orm_mode = True