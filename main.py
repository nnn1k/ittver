import asyncio
import os
import sys
import time


from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles

from backend.src.modules.rebuild import rebuild_schemas
from backend.views.base import backend_router
from frontend.router import router as frontend_router
import uvicorn
app = FastAPI()

app.include_router(backend_router)
app.include_router(frontend_router, include_in_schema=False)
frontend_dir = os.path.join(os.path.dirname(__file__), "frontend")
app.mount("/frontend", StaticFiles(directory=frontend_dir), name="static")


app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )


@app.middleware("http")
async def log_time_requests(request: Request, call_next):
    start_time = time.time()
    response = await call_next(request)
    duration = time.time() - start_time
    if request.url.path.startswith("/api"):
        print(
            f"{request.method} {request.url.path} - \n"
            f"Статус: {response.status_code} - Время обработки: {duration:.4f} секунд\n"
        )
    if response.status_code == 307 and "location" in response.headers:
        location = response.headers["location"]
        if location.startswith("http://"):
            response.headers["location"] = location.replace("http://", "https://")

    return response

rebuild_schemas()

if sys.platform == "win32":
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

if __name__ == '__main__':
    uvicorn.run(app, host='127.0.0.1', port=8000)
