from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.routes import agent_ws, frontend_ws, layer2, reports

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(agent_ws.router)
app.include_router(frontend_ws.router)
app.include_router(layer2.router)
app.include_router(reports.router)