from typing import Optional
from fastapi import FastAPI, File, UploadFile, Request
import utils
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles

# making app object 
app = FastAPI()

app.mount("/static", StaticFiles(directory= "static"), name="static")   #
template = Jinja2Templates(directory= "templates")    #

@app.get("/")
def home(request:Request):
    return template.TemplateResponse("index.html", {"request":request})

@app.post("/")
async def home_predict(request:Request, file:UploadFile= File(...)):
    # return utils.get_result(img_file= file)
    result= utils.get_result(img_file=file)
    return template.TemplateResponse("index.html", {"request":request, "result":result})

# prediction route 
@app.post("/predict")
async def predict(file:UploadFile= File(...)):
    return utils.get_result(img_file=file)

# some test route
@app.get("/tarek")
def tarek():
    return {"Message": "Hola from Tarek !"}