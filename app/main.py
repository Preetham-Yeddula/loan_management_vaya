from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from starlette.middleware.base import BaseHTTPMiddleware
import time
import json
from app.routes import loan

app = FastAPI()

class AddProcessTimeHeaderMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        start_time = time.time()
        response = await call_next(request)
        process_time = time.time() - start_time
        log_data = {
            "process_time": process_time,
            "status_code": response.status_code,
            "headers": dict(response.headers),
        }
        print(json.dumps(log_data))  # Log to console as JSON string
        return response

app.add_middleware(AddProcessTimeHeaderMiddleware)

app.include_router(loan.router, prefix="/loan", tags=["loan"])
@app.get("/")
async def root():
    return {"message": "Loan processing && management service"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
