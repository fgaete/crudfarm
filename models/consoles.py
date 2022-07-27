from numbers import Number
import string
from typing import Optional
from pydantic import BaseModel

class Console(BaseModel):
    id: Optional[str]
    name: str
    company: str
    year: int