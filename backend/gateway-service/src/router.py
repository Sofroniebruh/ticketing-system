from fastapi import APIRouter

from src.schemas import HealthResponse
from src.service import gateway_service

router = APIRouter()

@router.get(
    "/health",
    status_code=200,
    response_model=HealthResponse)
def health():
    return gateway_service.get_health_status()
