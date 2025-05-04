from fastapi import APIRouter
from app.database.neo4j_db import get_neo4j_data

router = APIRouter()

@router.get("/data")
async def get_graph_data():
    return get_neo4j_data()