from fastapi import APIRouter, HTTPException, Response, status

from app.database.fake_db import jogos
from app.schemas.jogo import JogoCreate, JogoUpdate

router = APIRouter(
    prefix="/jogos",
    tags=["Jogos"]
)


# GET /jogos
@router.get("")
def listar_jogos():
    return jogos


# GET /jogos/{id}
@router.get("/{id}")
def buscar_jogo(id: int):

    for jogo in jogos:
        if jogo["id"] == id:
            return jogo

    raise HTTPException(
        status_code=404,
        detail="Jogo não encontrado"
    )


# POST /jogos
@router.post("", status_code=status.HTTP_201_CREATED)
def criar_jogo(data: JogoCreate):

    novo_id = max([jogo["id"] for jogo in jogos], default=0) + 1

    novo_jogo = {
        "id": novo_id,
        "nome": data.nome,
        "tipo": data.tipo,
        "nota": data.nota,
        "review": data.review
    }

    jogos.append(novo_jogo)

    return novo_jogo

# PUT /jogos/{id}
@router.put("/{id}")
def atualizar_jogo(id: int, data: JogoUpdate):

    for index, jogo in enumerate(jogos):

        if jogo["id"] == id:

            jogos[index] = {
                "id": id,
                "nome": data.nome,
                "tipo": data.tipo,
                "nota": data.nota,
                "review": data.review
            }

            return jogos[index]

    raise HTTPException(
        status_code=404,
        detail="Jogo não encontrado"
    )


# DELETE /jogos/{id}
@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
def deletar_jogo(id: int):

    for index, jogo in enumerate(jogos):

        if jogo["id"] == id:
            jogos.pop(index)
            return Response(status_code=status.HTTP_204_NO_CONTENT)

    raise HTTPException(
        status_code=404,
        detail="Jogo não encontrado"
    )