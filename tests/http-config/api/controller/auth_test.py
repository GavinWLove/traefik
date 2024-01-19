from fastapi import FastAPI, Response, Request, APIRouter

router = APIRouter()


@router.get("/test")
async def read_item(request: Request, response: Response):
    # 假设这是你的数据获取逻辑
    print("============test===================")
    item = {"item_id": 100, "name": "xxxx"}
    for itemx in request.headers.items():
        print(itemx)
    # 设置响应头
    response.headers["bbbbb"] = "Some custom value bbbb"
    response.headers["aaaaa"] = "Another value aaaa"

    return item
