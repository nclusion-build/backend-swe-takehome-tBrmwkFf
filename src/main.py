from fastapi import FastAPI
from src.routes import games, leaderboard

app = FastAPI(title="Assignment API")

@app.get("/health")
def health():
    return {"status": "ok"}

# Register routers
app.include_router(games)
app.include_router(leaderboard)


// TODO: Add structured logging to Python server [ttt.feature.py.logging]