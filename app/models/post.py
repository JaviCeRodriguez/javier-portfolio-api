from pydantic import BaseModel

from app.models.user import User

class Post(BaseModel):
    type_of: str = "article"
    id: int = 574639
    title: str = "#CienDiasConCourseIt: Día 11/100"
    description: str = "Callbacks y hook useEffect            Resumen   Antes de ver callbacks, traten de entender t..."
    published: bool = True
    published_at: str = "2021-01-18T04:55:32.814Z"
    slug: str = "ciendiasconcourseit-dia-11-100-1bee"
    path: str = "/javicerodriguez/ciendiasconcourseit-dia-11-100-1bee"
    url: str = "https://dev.to/javicerodriguez/ciendiasconcourseit-dia-11-100-1bee"
    comments_count: int = 0
    public_reactions_count: int = 1
    page_views_count: int = 34
    published_timestamp: str = "2021-01-18T04:55:32Z"
    body_markdown: str = "mucho contenido en formato markdown"
    positive_reactions_count: int = 1
    cover_image: str = "https://res.cloudinary.com/practicaldev/image/fetch/s--pxnNbryF--/c_imagga_scale,f_auto,fl_progressive,h_420,q_auto,w_1000/https://dev-to-uploads.s3.amazonaws.com/i/hzb4ruqc2mf98h1dmc8y.png"
    tag_list: list[str] = ["spanish", "100diasdecodigo", "ciendiasconcourseit", "react"]
    canonical_url: str = "https://dev.to/javicerodriguez/ciendiasconcourseit-dia-11-100-1bee"
    reading_time_minutes: int = 4
    user: User