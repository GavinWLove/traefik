from fastapi import APIRouter

from api.controller.yaml_config import router as yaml_config_router
from api.controller.auth_test import router as auth_test_router
from api.controller.auth import router as auth_router


router = APIRouter()
router.include_router(auth_router, tags=["auth"], prefix="/auth")
router.include_router(auth_test_router, tags=["auth"], prefix="/authtest")
router.include_router(yaml_config_router, tags=["confi"], prefix="/config")
