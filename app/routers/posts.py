from fastapi import APIRouter

from app.models.post import Post

router = APIRouter(
    prefix="/api/items",
    tags=["posts"]
)

@router.get("/", response_model=list[Post])
async def read_posts(limit: int = 6):
    return {"message": "posts"}