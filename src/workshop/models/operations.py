from datetime import date
from decimal import Decimal
from enum import Enum
from typing import Optional

from pydantic import BaseModel


class OperationKind(str, Enum):
    INCOME = 'income'
    EXPENSE = 'expense'


class Operations(BaseModel):
    id: int
    date: date
    kind: OperationKind
    amount: Decimal
    description: Optional[str]

    class Config:
        orm_mode = True
