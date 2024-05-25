from fastapi import APIRouter
from app.controllers.loan_controller import LoanController
from app.models.loan_application import LoanApplication
from uuid import UUID

router = APIRouter()
controller = LoanController()

@router.post("/apply")
async def submit_application(application: LoanApplication):
    return controller.submit_application(application)

@router.get("/status/{application_id}")
async def get_application_status(application_id: int):
    return controller.get_application_status(application_id)

@router.put("/update/{application_id}")
async def update_application(application_id: int, updated_application: LoanApplication):
    return controller.update_application(application_id, updated_application)
