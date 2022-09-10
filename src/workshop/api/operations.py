from typing import List

import tables
from database import get_session
from fastapi import APIRouter, Depends
from models.operations import Operations
from sqlalchemy.orm import Session

router = APIRouter(prefix='/operations')


@router.get('/', response_model=List[Operations])
def get_operations(session: Session = Depends(get_session)):
    operations = (
        session.query(tables.Operation).all()
    )
    return operations
