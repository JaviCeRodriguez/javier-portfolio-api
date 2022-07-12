from fastapi import APIRouter, status

from db.database import retrieve_posts
from models.post import Post

router = APIRouter(
    prefix="/api/posts",
    tags=["posts"]
)

@router.get("/", response_model=list[Post], status_code=status.HTTP_200_OK)
async def read_posts(limit: int = 6, page: int = 0):
    posts = await retrieve_posts(limit=limit, page=page)
    return posts