import requests
import motor.motor_asyncio
from decouple import config

MONGO_DETAILS = config("MONGO_DETAILS")
client = motor.motor_asyncio.AsyncIOMotorClient(MONGO_DETAILS)
database = client.portfolio

headers = {
    'Accept': 'application/json',
    'api-key': config("DEV_TO_API_KEY")
}

post_collection = database.get_collection("posts_collection")

def helper(doc) -> dict:
    return { key: value for key, value in doc.items() }

async def populate_posts():
    posts = await retrieve_posts()
    url = "https://dev.to/api/articles/me"
    req = requests.get(url, headers=headers)

    if len(posts) == 0: # Populate if posts in db is empty
        for post in req.json():
            new_post = await add_post(post)
            if new_post: print(f"Agregado {new_post['title']} (id: {new_post['id']})")
    elif len(posts) < len(req.json()): # Populate if length req objects is less than posts in db
        pass # TODO
    else:
        print(f"No hace falta popular posts_collection")

async def retrieve_posts():
    posts = []
    async for post in post_collection.find():
        posts.append(helper(post))
    return posts

async def add_post(post_data: dict) -> dict:
    post = await post_collection.insert_one(post_data)
    new_post = await post_collection.find_one({ "_id": post.inserted_id })
    return helper(new_post)
