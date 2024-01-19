from fastapi import FastAPI, Response, Request, APIRouter

router = APIRouter()


@router.get("/token")
async def read_item(request: Request, response: Response):
    # 假设这是你的数据获取逻辑
    print("============token===================")
    item = {"item_id": 1, "name": "Foo"}
    for itemx in request.headers.items():
        print(itemx)
    # 设置响应头
    response.headers["X-Custom-Header"] = "Some custom value"
    response.headers["jk-Header"] = "ffffff"
    response.headers["jk-xxxx"] = "xxxx"

    return item
