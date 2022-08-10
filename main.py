from typing import Optional
from fastapi import FastAPI, File, UploadFile, Request, Form
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

# @app.post("/sub")
# async def handle_form(top_right_lang: str = Form(...)):
#     print(top_right_lang)

# some test route
@app.get("/tarek")
async def tarek_home(request:Request):
    return template.TemplateResponse("test-code.html", {"request": request})

@app.post("/tarek")
async def tarek(request:Request, top_left_lang: str= Form(...), top_left_long: str= Form(...)):
    data = {
        "t_left_lang": top_left_lang,
        "t_left_long": top_left_long
    }
    # return template.TemplateResponse("test-code.html", {"request":request, "top_right_lang": top_right_lang, "top_right_long": top_right_long})
    return template.TemplateResponse("test-code.html", {"request":request, "data":data})