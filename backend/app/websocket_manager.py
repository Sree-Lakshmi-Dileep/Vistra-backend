from typing import Dict
from fastapi import WebSocket

class ConnectionManager:
    def __init__(self):
        self.agents: Dict[str, WebSocket] = {}
        self.frontends: Dict[str, WebSocket] = {}

    async def connect_agent(self, device_id: str, websocket: WebSocket):
        await websocket.accept()
        self.agents[device_id] = websocket

    async def connect_frontend(self, device_id: str, websocket: WebSocket):
        await websocket.accept()
        self.frontends[device_id] = websocket

    def disconnect_agent(self, device_id: str):
        self.agents.pop(device_id, None)

    def disconnect_frontend(self, device_id: str):
        self.frontends.pop(device_id, None)

    async def send_to_agent(self, device_id: str, data: dict):
        if device_id in self.agents:
            await self.agents[device_id].send_json(data)

    async def send_to_frontend(self, device_id: str, data: dict):
        if device_id in self.frontends:
            await self.frontends[device_id].send_json(data)

manager = ConnectionManager()