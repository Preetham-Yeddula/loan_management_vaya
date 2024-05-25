from fastapi import APIRouter, HTTPException
from app.controllers.loan_controller import LoanController
from app.models.loan_application import LoanApplication
from uuid import UUID

router = APIRouter()
controller = LoanController()

@router.post("/apply")
async def submit_application(application: LoanApplication):
    try:
        return await controller.submit_application(application)
    except HTTPException as e:
        return e
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    

@router.get("/status/{application_id}")
async def get_application_status(application_id: int):
    try:
        return await controller.get_application_status(application_id)
    except HTTPException as e:
        return e
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
    

@router.put("/update/{application_id}")
async def update_application(application_id: int, updated_application: LoanApplication):
    try:
        return await controller.update_application(application_id, updated_application)
    except HTTPException as e:
        return e
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
    
