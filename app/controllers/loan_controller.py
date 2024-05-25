from fastapi import HTTPException
from app.Utils.DictDataStore import DictDataStore
from app.Utils.MongoDataStore import MongoDataStore
from app.models.loan_application import LoanApplication
from app.repositories.loan_repository import LoanRepository
from app.services.risk_assessment import RiskAssessment

class LoanController:
    def __init__(self):
        self.repository = LoanRepository(data_store=MongoDataStore("loan_db", "loan_applications"))
        self.risk_assessment = RiskAssessment()

    async def submit_application(self, application: LoanApplication):
        try:
            application.status = "Approved" if self.risk_assessment.approve_or_reject(application) else "Rejected"
            await self.repository.save_application(application)
            return application
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    async def get_application_status(self, application_id):
        try:
            return await self.repository.get_application(application_id)
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    async def update_application(self, application_id, updated_application: LoanApplication):
        try:
            updated_application.status = "Approved" if self.risk_assessment.approve_or_reject(updated_application) else "Rejected"
            await self.repository.update_application(application_id, updated_application)
            return updated_application
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))
