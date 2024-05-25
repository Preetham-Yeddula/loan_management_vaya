from typing import Dict, Type
from uuid import UUID
from app.models.loan_application import LoanApplication
from app.Utils.DataStoreInterface import IDataStore

class LoanRepository:
    def __init__(self, data_store: Type[IDataStore]):
        self.data_store = data_store

    def save_application(self, application: LoanApplication):
        self.data_store.add(str(application.id), application)

    def get_application(self, application_id: UUID):
        application = self.data_store.get(str(application_id))
        if application:
            return {"id": str(application_id), "status": application.status}
        return None

    def update_application(self, application_id: UUID, application: LoanApplication):
        self.data_store.update(str(application_id), application)

    def delete_application(self, application_id: UUID):
        self.data_store.remove(str(application_id))