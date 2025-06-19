import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

from fastapi import APIRouter,FastAPI
from src.routes import login,cliente,favorito,produtos

app = FastAPI(title="Api Cliente Produto")
router = APIRouter()

app.include_router(login.router)
app.include_router(cliente.router)
app.include_router(favorito.router)
app.include_router(produtos.router)