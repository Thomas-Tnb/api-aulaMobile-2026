from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routes.auth import router as auth_router
from app.routes.jogos import router as jogos_router


app = FastAPI(
    title="Jogos API",
    version="1.0.0"
)

# Allow all origins (any IP/domain)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth_router)
app.include_router(jogos_router)


@app.get("/")
def root():
    return {"message": "API running"}