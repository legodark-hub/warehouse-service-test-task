from fastapi import APIRouter
from fastapi import Depends
from src.api.services.movement import MovementService
from src.schemas.movement import MovementInfoResponse


router = APIRouter(prefix="/movement")

@router.get("/{movement_id}", response_model=MovementInfoResponse)
async def get_movement_info(movement_id: str, service: MovementService = Depends(MovementService)):
    movement_info = await service.get_movement_info(movement_id)
    return MovementInfoResponse(payload=movement_info)
