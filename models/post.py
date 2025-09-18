from pydantic import BaseModel


class PostResponse(BaseModel):
    userId: int
    id: int
    title: str
    body: str
