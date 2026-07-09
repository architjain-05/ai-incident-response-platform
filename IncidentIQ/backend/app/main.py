from fastapi import FastAPI

from .api.logs import router as logs_router

app = FastAPI(title="IncidentIQ Log API")
app.include_router(logs_router)
