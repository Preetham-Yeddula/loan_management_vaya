from app.Utils.DictDataStore import DictDataStore
from app.Utils.MongoDataStore import MongoDataStore
from app.models.loan_application import LoanApplication
from app.repositories.loan_repository import LoanRepository
from app.services.risk_assessment import RiskAssessment

class LoanController:
    def __init__(self):
        self.repository = LoanRepository(data_store=MongoDataStore("loan_db", "loan_applications"))
        self.risk_assessment = RiskAssessment()

    def submit_application(self, application: LoanApplication):
        application.status = "Approved" if self.risk_assessment.approve_or_reject(application) else "Rejected"
        self.repository.save_application(application)
        return application

    def get_application_status(self, application_id):
        return self.repository.get_application(application_id)

    def update_application(self, application_id, updated_application: LoanApplication):
        updated_application.status = "Approved" if self.risk_assessment.approve_or_reject(updated_application) else "Rejected"
        self.repository.update_application(application_id, updated_application)
        return updated_application
