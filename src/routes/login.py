from datetime import timedelta
from fastapi import APIRouter

router = APIRouter(prefix="/login",tags=["Login"])

@router.post('/')
def login(request):
    return request
