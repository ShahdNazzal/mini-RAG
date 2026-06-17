from fastapi import FastAPI, APIRouter
import os

# إنشاء التطبيق
app = FastAPI()

# إنشاء router
base_router = APIRouter(
    prefix="/api/v1",
    tags=["api_v1"],
)

# endpoint
@base_router.get("/")
async def welcome():
    app_name = os.getenv('APP_NAME', 'Mini RAG App')
    app_version = os.getenv('APP_VERSION', '1.0.0')
    
    return {
        "app_name": app_name,
        "app_version": app_version,
    }

# ربط الراوتر مع التطبيق
app.include_router(base_router)