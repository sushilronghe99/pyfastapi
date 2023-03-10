from fastapi import FastAPI, File, UploadFile
import requests


from bg import remove


from PIL import Image
from io import BytesIO
import base64
from pydantic import BaseModel


class Item(BaseModel):
    imageName: str
    imageData: str
    

# Convert Image to Base64 
def im_2_b64(image):
    buff = BytesIO()
    image.save(buff, format="PNG")
    img_str = base64.b64encode(buff.getvalue())
    #print(img_str)
    return img_str

# Convert Base64 to Image
def b64_2_img(data):
    buff = BytesIO(base64.b64decode(data))
    return Image.open(buff)



app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.post("/data")
def function1(data:Item):
    return {"Hello": data}

@app.post("/removeBg")
def handler(data:Item):
    #url = "https://unsplash.com/photos/E3LcqpQxtTU/download?force=true&w=640"
    #response = requests.get(url)
  
    #input_path = 'muh.jpg'
    #output_path = 'output.png'

    input = b64_2_img(data.imageData)
    output = remove(input)
    #buffered = BytesIO()
    #output.save(buffered)
    
    im_b64 = im_2_b64(output)
    #print(im_b64)
    #img_str = base64.b64encode(buffered.getvalue())
    return "data:image/png:base64," + im_b64.decode("utf-8")
    #return {"content": im_b64.decode("utf-8")}