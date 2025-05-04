from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routes import line_chart, graph, hotspot

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],  # Frontend URL
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(line_chart.router, prefix="/api/line")
app.include_router(graph.router, prefix="/api/graph")
app.include_router(hotspot.router, prefix="/api/hotspot")

@app.get("/")
async def root():
    return {"message": "Interactive Charts API"}