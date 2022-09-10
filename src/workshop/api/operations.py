from typing import List

from fastapi import APIRouter, Depends
from models.operations import Operations
from services.operations import OperationService

router = APIRouter(prefix='/operations')


@router.get('/', response_model=List[Operations])
def get_operations(service: OperationService = Depends()):
    return service.get_list()
