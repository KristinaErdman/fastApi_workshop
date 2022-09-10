from typing import List

from database import get_session
from fastapi import Depends
from sqlalchemy.orm import Session
from tables import Operation


class OperationService:
    def __init__(self, session: Session = Depends(get_session)):
        self.session = session

    def get_list(self) -> List[Operation]:
        operations = (
            self.session.query(Operation).all()
        )
        return operations
