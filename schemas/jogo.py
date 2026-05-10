from pydantic import BaseModel, Field


class JogoBase(BaseModel):
    nome: str
    tipo: str
    nota: int = Field(..., ge=0, le=10)
    review: str


class JogoCreate(JogoBase):
    pass


class JogoUpdate(JogoBase):
    pass