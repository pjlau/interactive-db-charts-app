from fastapi import APIRouter
from app.database.mongodb_db import get_mongo_data

router = APIRouter()

@router.get("/data")
async def get_hotspot_data():
    return get_mongo_data()