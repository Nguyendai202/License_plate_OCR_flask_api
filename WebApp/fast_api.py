from fastapi import FastAPI, File, UploadFile
from fastapi.responses import HTMLResponse
from starlette.requests import Request
from starlette.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import os
import uvicorn
from io import BytesIO
import cv2
import numpy as np 
from PIL import Image 
from detect_and_ocr import OCR
import tensorflow as tf

app = FastAPI()
BASE_PATH = os.getcwd()
UPLOAD_PATH = os.path.join(BASE_PATH,'3_WebApp/static/uploadnew/')

app.mount("/static", StaticFiles(directory="C:/Users/Admin/project_bsx/3_WebApp/static/"), name='static')

templates = Jinja2Templates(directory="C:/Users/Admin/project_bsx/3_WebApp/templates/")

# async def my_view(request: Request):
#     context = {"request": request}
#     return templates.TemplateResponse("my_template.html", context=context)

@app.get("/")
async def read_item(request: Request, id: str = ""):
    return templates.TemplateResponse("index.html", {"request": request, "id": id}) # hiện thị template

@app.post("/uploadfile/")
async def create_upload_file(image_file: UploadFile = File(...)):
    filename = image_file.filename
    file_type = filename.split(".")[-1]
    
    if file_type not in ["jpg", "jpeg", "png"]:
        return {"error": "Unsupported file type"}
    try:
        with open (os.path.join(UPLOAD_PATH, filename),"wb") as f:
            # path=upload_path
            contents = await image_file.read()
            nparr = np.frombuffer(contents,np.uint8)# chuyển sang numpy 
            img = cv2.imdecode(nparr,cv2.IMREAD_COLOR)# giải mã ảnh > đối tượng numpy có màu sắc 
            img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
            buffered= BytesIO()
            PIL_image = Image.fromarray(img)
            PIL_image.save(buffered, format='JPEG')
            f.write(buffered.getvalue())
        
        text = OCR(os.path.join(UPLOAD_PATH, filename),filename)
    except Exception as e:
        return {"error": str(e)}
    # context = {"request": "3_WebApp/templates/index.htmll", "upload": True, "upload_image": filename, "text": text}
    return {"text":text}
    # return templates.TemplateResponse("index.html", {"upload": True, "upload_image": filename, "text": text})
if __name__ == '__main__':
    print("In processing...")
    uvicorn.run(app=app, host="127.0.0.2", port=8000)
