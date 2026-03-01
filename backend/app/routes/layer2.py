from fastapi import APIRouter
from app.database import create_scan, complete_scan, save_file, get_user_by_device

router = APIRouter()

@router.post("/layer2-alert/{device_id}")
async def layer2_alert(device_id: str, data: dict):

    user_id = get_user_by_device(device_id)

    scan_id = create_scan(user_id, device_id)

    save_file(
        scan_id=scan_id,
        file_path=data["file_path"],
        is_malicious=True,
        layer="layer2"
    )

    complete_scan(scan_id)

    return {"status": "stored"}