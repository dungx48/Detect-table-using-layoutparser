import os
import cv2
import time
from PIL import Image
from io import BytesIO
from detect_table import detect_table
from fastapi.responses import FileResponse
from fastapi import FastAPI, Form, UploadFile, File
from starlette.responses import StreamingResponse, FileResponse
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

def load_image_into_array(data):
    return Image.open(BytesIO(data))

@app.post("/detect")
async def _detect_table(file: UploadFile = File(...)):
    
    image = load_image_into_array(await file.read())
    img_processed = detect_table(image)

    img_name = file.filename
    path = "/home/vdungx/Desktop/detect_table_KTTV/layout-parser/detected_image/"
    img_path = os.path.join(path, img_name)
    img_processed.save(img_path)

    # return FileResponse(img_path, media_type="image/png")
    print("-------------------------line46-----------")
    print({"image":f'http://localhost:8000/image?image={img_name}'})
    return f'http://localhost:8000/image?image={img_name}'

@app.get("/image")
async def _image(image:str):
    img_path = f"/home/vdungx/Desktop/detect_table_KTTV/layout-parser/detected_image/{image}"
    print("------------------------line53-----------")
    return FileResponse(img_path)