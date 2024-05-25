from typing import Dict, Type
from uuid import UUID

from fastapi import HTTPException
from app.models.loan_application import LoanApplication
from app.Utils.DataStoreInterface import IDataStore

class LoanRepository:
    def __init__(self, data_store: Type[IDataStore]):
        self.data_store = data_store

    async def save_application(self, application: LoanApplication):
        try:
            await self.data_store.add({"_id": str(application.id), **application.__dict__})
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    async def get_application(self, application_id: UUID):
        try:
            application = await self.data_store.get(str(application_id))
            if application:
                return {"id": str(application_id), "status": application}
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))
        

    async def update_application(self, application_id: UUID, application: LoanApplication):
        try:
            await self.data_store.update(str(application_id), application.__dict__)
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

        
