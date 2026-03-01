from fastapi import APIRouter, WebSocket, WebSocketDisconnect
from app.websocket_manager import manager

router = APIRouter()

@router.websocket("/ws/frontend/{device_id}")
async def frontend_ws(websocket: WebSocket, device_id: str):

    await manager.connect_frontend(device_id, websocket)

    try:
        while True:
            message = await websocket.receive_json()
            event = message.get("event")

            if event == "START_SCAN":
                await manager.send_to_agent(device_id, message)

            elif event == "DELETE_FILE":
                await manager.send_to_agent(device_id, message)

    except WebSocketDisconnect:
        manager.disconnect_frontend(device_id)