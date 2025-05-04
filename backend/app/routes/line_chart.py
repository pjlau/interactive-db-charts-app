from fastapi import APIRouter
from app.database.sqlite_db import get_sqlite_data

router = APIRouter()

@router.get("/data")
async def get_line_chart_data():
    return get_sqlite_data()