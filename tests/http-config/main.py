from fastapi import FastAPI, Request, Response, status
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse
from starlette.exceptions import HTTPException
from starlette.middleware.cors import CORSMiddleware
from api.routes import router2 as front_router
from api.routes import router as api_router
from logger import DVStreamHandler

# from core.health_probe import router as health_router
from core.settings import settings
import logging




# 日志配置
logging.basicConfig(level=settings.LOG_LEVEL)
console_handler = DVStreamHandler()
# console_handler.setLevel(settings.LOG_LEVEL)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
console_handler.setFormatter(formatter)
root_logger = logging.getLogger()
for handler in root_logger.handlers[:]:
    root_logger.removeHandler(handler)
root_logger.addHandler(console_handler)

uvicorn_access_logger = logging.getLogger("uvicorn.access")
for handler in uvicorn_access_logger.handlers[:]:
    uvicorn_access_logger.removeHandler(handler)
uvicorn_access_logger.addHandler(console_handler)

logging.getLogger("uvicorn.error").setLevel(settings.LOG_LEVEL)
logging.getLogger("uvicorn.access").setLevel(settings.LOG_LEVEL)
logging.getLogger("uvicorn.asgi").setLevel(settings.LOG_LEVEL)



# FastAPI配置
app = FastAPI(**settings.fastapi_kwargs)
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.allowed_hosts,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(api_router, prefix=settings.api_prefix)
app.include_router(front_router)
# app.include_router(health_router)


# 捕获参数 验证错误
@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request: Request, exc: RequestValidationError):
    return JSONResponse(
        status_code=status.HTTP_200_OK,
        content={
            "code": 400,
            "data": {"tip": exc.errors()},
            # "body": exc.body,
            "msg": "参数不全或参数错误",
        },
    )


@app.exception_handler(HTTPException)
async def http_exception_handler(request: Request, exc: HTTPException):
    return JSONResponse(
        status_code=status.HTTP_200_OK,
        content={"code": 400, "data": {"tip": exc.detail}, "msg": "请求异常"},
    )

#
# @app.exception_handler(OpenAIError)
# async def http_exception_handler(request: Request, exc: OpenAIError):
#     return JSONResponse(
#         status_code=status.HTTP_200_OK,
#         content={"code": 500, "data": None, "msg": "openAI 调用失败，请检查。"},
#     )


# 捕获全部异常
@app.exception_handler(Exception)
async def all_exception_handler(request: Request, exc: Exception):
    return JSONResponse(
        status_code=500,
        content={"code": 500, "data": {"tip": "服务器错误"}, "msg": "服务器错误"},
    )


# env配置打印
system_logger = logging.getLogger("uvicorn.error")
system_logger.info(f"=====================env ===========================")
system_logger.info(f"LOG_LEVEL: {settings.LOG_LEVEL}")
system_logger.info(f"REDIS_DATABASE: {settings.REDIS_DATABASE}")
system_logger.info(f"REDIS_HOST: {settings.REDIS_HOST}")
system_logger.info(f"VECTOR_DB_HOST: {settings.VECTOR_DB_HOST}")
system_logger.info(f"VECTOR_DB_PORT: {settings.VECTOR_DB_PORT}")
system_logger.info(f"VOLC_HOST: {settings.VOLC_HOST}")
system_logger.info(f"VOLC_REGION: {settings.VOLC_REGION}")
system_logger.info(f"=====================env ===========================")
