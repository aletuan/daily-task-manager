from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from contextlib import asynccontextmanager

from .routers import tasks_router, users_router, categories_router
from .database.session import engine
from .models.base import Base


@asynccontextmanager
async def lifespan(app: FastAPI):
    # Startup
    # Create database tables
    Base.metadata.create_all(bind=engine)
    yield
    # Shutdown
    pass


# Create FastAPI app
app = FastAPI(
    title="Daily Task Manager API",
    description="A modern API for efficient daily task management with drag-and-drop functionality",
    version="1.0.0",
    lifespan=lifespan
)

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # In production, specify actual origins
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
app.include_router(tasks_router, prefix="/api/v1")
app.include_router(users_router, prefix="/api/v1")
app.include_router(categories_router, prefix="/api/v1")


@app.get("/")
async def root():
    """Root endpoint"""
    return {
        "message": "Daily Task Manager API",
        "version": "1.0.0",
        "docs": "/docs",
        "redoc": "/redoc"
    }


@app.get("/health")
async def health_check():
    """Health check endpoint"""
    return {"status": "healthy"} 