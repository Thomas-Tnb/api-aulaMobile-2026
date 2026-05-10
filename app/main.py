from fastapi import FastAPI
from app.routes.auth import router as auth_router
from app.routes.jogos import router as jogos_router

app = FastAPI(
    title="Jogos API",
    version="1.0.0"
)

app.include_router(auth_router)
app.include_router(jogos_router)


@app.get("/")
def root():
    return {"message": "API running"}