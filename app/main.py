from fastapi import FastAPI

from app.db import database
from app.routers import posts

app = FastAPI()
app.include_router(posts.router)

@app.on_event("startup")
async def startup():
    await database.populate_posts()
    print({"message": "populating database"})


@app.on_event("shutdown")
async def shutdown():
    print({"message": "API Off!"})


@app.get("/api")
async def root():
    return {"message": "Hola! Querés un mate? 🧉"}