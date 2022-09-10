from typing import List

from fastapi import Depends, HTTPException, status
from sqlalchemy.orm import Session

from ..database import get_session
from ..models.operations import OperationKind, OperationCreate, OperationUpdate
from ..tables import Operation


class OperationService:
    def __init__(self, session: Session = Depends(get_session)):
        self.session = session

    def get_list(self, kind: OperationKind = None) -> List[Operation]:
        query = self.session.query(Operation)
        if kind:
            query = query.filter_by(kind=kind)
        operations = query.all()
        return operations

    def get(self, operation_id: int) -> Operation:
        operation = self.session.query(Operation).get(operation_id)
        if not operation:
            raise HTTPException(status.HTTP_404_NOT_FOUND)
        else:
            return operation

    def create(self, operation_data: OperationCreate) -> Operation:
        operation = Operation(**operation_data.dict())
        self.session.add(operation)
        self.session.commit()
        return operation

    def update(self, operation_id: int, operation_data: OperationUpdate) -> Operation:
        operation = self.get(operation_id)
        for field, value in operation_data:
            setattr(operation, field, value)
        self.session.commit()
        return operation

    def delete(self, operation_id: int):
        operation = self.get(operation_id)
        self.session.delete(operation)
        self.session.commit()
