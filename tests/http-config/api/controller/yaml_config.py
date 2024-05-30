from fastapi import FastAPI, Response, Request, APIRouter
import yaml

router = APIRouter()


@router.get("/yaml")
async def get_yaml_content_dynamic():

    with open("router2.yaml", "r", encoding="utf-8") as file:
        data = yaml.safe_load(file)
    return data
