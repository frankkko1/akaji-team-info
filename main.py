from fastapi import FastAPI
from fastapi.responses import JSONResponse
import requests

app = FastAPI()

@app.get("/info")
def proxy_info(uid: str):
    try:
        response = requests.get(f"https://rzx-team-api-info.vercel.app/info?uid={uid}")
        data = response.json()
        if "BY API" in data:
            data["BY API"] = "@zox_26 AND @p_r_t_1"
        return JSONResponse(content=data)
    except Exception as e:
        return {"error": "فشل الاتصال بالسيرفر الأصلي"}
