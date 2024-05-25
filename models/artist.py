from typing import List

from models.base_model import BaseModel


class Artist(BaseModel):
    id: str
    name: str
    genres: List[str]
