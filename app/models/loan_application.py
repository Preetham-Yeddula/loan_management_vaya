from pydantic import BaseModel, Field
from uuid import uuid4, UUID

class LoanApplication(BaseModel):
    id: int 
    name: str
    credit_score: int
    loan_amount: float
    loan_purpose: str
    income: float
    employment_status: str
    status: str = "Pending"
