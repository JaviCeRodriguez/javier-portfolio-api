from pydantic import BaseModel

class User(BaseModel):
    name: str = "Javier Rodriguez"
    username: str = "javicerodriguez"
    twitter_username: str = "javicerodriguez"
    github_username: str = "JaviCeRodriguez"
    website_url: str = "https://javo.dev.ar/"
    profile_image: str = "https://res.cloudinary.com/practicaldev/image/fetch/s--mDyEkL3d--/c_fill,f_auto,fl_progressive,h_640,q_auto,w_640/https://dev-to-uploads.s3.amazonaws.com/uploads/user/profile_image/518659/b78db08c-da18-4513-a585-a0023fcdbeff.jpg"
    profile_image_90: str = "https://res.cloudinary.com/practicaldev/image/fetch/s--X-6E-Mi---/c_fill,f_auto,fl_progressive,h_90,q_auto,w_90/https://dev-to-uploads.s3.amazonaws.com/uploads/user/profile_image/518659/b78db08c-da18-4513-a585-a0023fcdbeff.jpg"
