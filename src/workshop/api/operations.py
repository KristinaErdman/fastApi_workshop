from typing import List, Optional

from fastapi import APIRouter, Depends, Response, status, Body, Query, Path

from ..models.auth import User
from ..models.operations import Operation, OperationKind, OperationCreate, OperationUpdate
from ..services.auth import get_current_user
from ..services.operations import OperationService

router = APIRouter(prefix='/operations', tags=["Operations", ])


@router.get('/', response_model=List[Operation])
def get_operations(
        kind: Optional[OperationKind] = Query(default=None),
        user: User = Depends(get_current_user),
        service: OperationService = Depends()
):
    """
    Получение списка операций текущего пользователя

    - **kind**: Фильтр по виду операций
    """
    return service.get_list(user.id, kind)


@router.get('/{operation_id}', response_model=Operation)
def get_operation(
        operation_id: int = Path(),
        user: User = Depends(get_current_user),
        service: OperationService = Depends()
):
    return service.get(user.id, operation_id)


@router.post('/', response_model=Operation)
def create_operation(
        operation_data: OperationCreate = Body(),
        user: User = Depends(get_current_user),
        service: OperationService = Depends()
):
    return service.create(user.id, operation_data)


@router.put('/{operation_id}', response_model=Operation)
def update_operation(
        operation_id: int = Path(),
        operation_data: OperationUpdate = Body(),
        user: User = Depends(get_current_user),
        service: OperationService = Depends()
):
    return service.update(operation_id, operation_data, user.id)


@router.delete('/{operation_id}', status_code=status.HTTP_204_NO_CONTENT)
def delete_operation(
        operation_id: int = Path(),
        user: User = Depends(get_current_user),
        service: OperationService = Depends()
):
    service.delete(operation_id, user.id)
    return Response(status_code=status.HTTP_204_NO_CONTENT)
