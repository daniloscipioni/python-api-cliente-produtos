from pydantic import BaseModel,Field,EmailStr

class Cliente(BaseModel):
  
    nome: str  = Field(..., min_length=5, max_length=50,
                      description="Nome do cliente")

    email: EmailStr = Field(..., description="Endereço de email do cliente")
    
    password: str

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "nome": "Nome do Cliente",
                    "email": "email@cliente.com.br",
                    "password": "p@ssword",
                }
            ]
        }
    }
