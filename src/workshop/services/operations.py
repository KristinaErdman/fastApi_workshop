from typing import List

from fastapi import Depends, HTTPException, status
from sqlalchemy.orm import Session

from ..database import get_session
from ..models.operations import OperationKind, OperationCreate, OperationUpdate
from ..tables import Operation


class OperationService:
    def __init__(self, session: Session = Depends(get_session)):
        self.session = session

    def get_list(self, user_id: int, kind: OperationKind = None) -> List[Operation]:
        query = self.session.query(Operation).filter_by(user_id=user_id)
        if kind:
            query = query.filter_by(kind=kind)
        operations = query.all()
        return operations

    def get(self, operation_id: int, user_id: int, ) -> Operation:
        operation = self.session.query(Operation).filter_by(id=operation_id, user_id=user_id)
        if not operation:
            raise HTTPException(status.HTTP_404_NOT_FOUND)
        else:
            return operation

    def create_many(self, operations_data: List[OperationCreate], user_id: int) -> List[Operation]:
        operations = list(
            map(lambda operation_data: Operation(**operation_data.dict(), user_id=user_id), operations_data)
        )
        self.session.add_all(operations)
        self.session.commit()
        return operations

    def create(self, user_id: int, operation_data: OperationCreate) -> Operation:
        operation = Operation(**operation_data.dict(), user_id=user_id)
        self.session.add(operation)
        self.session.commit()
        return operation

    def update(self, operation_id: int, operation_data: OperationUpdate, user_id: int, ) -> Operation:
        operation = self.get(operation_id)
        if operation.user_id != user_id:
            raise HTTPException(status.HTTP_403_FORBIDDEN)
        for field, value in operation_data:
            setattr(operation, field, value)
        self.session.commit()
        return operation

    def delete(self, operation_id: int, user_id: int, ):
        operation = self.get(operation_id)
        if operation.user_id != user_id:
            raise HTTPException(status.HTTP_403_FORBIDDEN)
        self.session.delete(operation)
        self.session.commit()
