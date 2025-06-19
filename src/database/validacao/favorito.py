from typing import Optional
from pydantic import BaseModel,Field,EmailStr

class Favorito(BaseModel):
  
    id_produto: int
    review: Optional[str]
    user_id: int

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "id_produto": 1,
                    "review": "Review do Favorito",
                    "user_id": 1,
                }
            ]
        }
    }
