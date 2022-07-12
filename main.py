from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from db import database
from routers import posts

app = FastAPI()


origins = [
    "https://javo.dev.ar/",
    "http://localhost:3000/"
]

app.include_router(posts.router)
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

@app.on_event("startup")
async def startup():
    print({"message": "🚧 populating database"})
    await database.populate_posts()
    print({"message": "✅ populating ok!"})


@app.on_event("shutdown")
async def shutdown():
    print({"message": "API Off!"})


@app.get("/api")
async def root():
    return {"message": "Hola! Querés un mate? 🧉"}