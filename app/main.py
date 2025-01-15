from fastapi import FastAPI, HTTPException
from fastapi.staticfiles import StaticFiles
from fastapi.responses import JSONResponse, RedirectResponse
from pathlib import Path
from loguru import logger
from contextlib import asynccontextmanager

# Configure loguru
logger.add(
    "logs/app.log",  # Log file path
    rotation="500 MB",  # Rotate file when it reaches 500MB
    retention="10 days",  # Keep logs for 10 days
    level="INFO",
    format="{time:YYYY-MM-DD HH:mm:ss} | {level} | {message}",
    backtrace=True,
    diagnose=True
)

# Configuration
STATIC_DIR = Path("static")
HOST = "0.0.0.0"
PORT = 8800

@asynccontextmanager
async def lifespan(app: FastAPI):
    # Startup
    logger.info("Starting up the application")
    yield
    # Shutdown
    logger.info("Shutting down the application")

# Create and configure FastAPI app
app = FastAPI(
    title="Static File Server",
    description="A simple API for serving static files",
    version="1.0.0",
    lifespan=lifespan
)

# Ensure static directory exists
STATIC_DIR.mkdir(exist_ok=True)

# Mount static files handler
app.mount("/static", StaticFiles(directory=STATIC_DIR), name="static")

# Root path handler
@app.get("/")
async def root():
    return {"message": "Welcome to the Static File Server. Access files at /static/{filename}"}

# Redirect non-static paths to static
@app.get("/{file_path:path}")
async def redirect_to_static(file_path: str):
    if not file_path.startswith("static/"):
        logger.info(f"Redirecting request from /{file_path} to /static/{file_path}")
        return RedirectResponse(url=f"/static/{file_path}")
    return HTTPException(status_code=404, detail="File not found")

@app.exception_handler(HTTPException)
async def http_exception_handler(request, exc):
    logger.error(f"HTTP Exception: {exc.detail}")
    return JSONResponse(
        status_code=exc.status_code,
        content={"message": exc.detail},
    )

# Health check endpoint
@app.get("/health")
async def health_check():
    return {"status": "healthy"}


if __name__ == "__main__":
    import uvicorn
    logger.info(f"Starting server on {HOST}:{PORT}")
    uvicorn.run("main:app", host=HOST, port=PORT)