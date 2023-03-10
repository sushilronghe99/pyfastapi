import requests


from rembg.bg import remove
from rembg.session_factory import new_session

from PIL import Image
from io import BytesIO
import base64


# Convert Image to Base64 
def im_2_b64(image):
    buff = BytesIO()
    image.save(buff, format="PNG")
    img_str = base64.b64encode(buff.getvalue())
    return img_str

# Convert Base64 to Image
def b64_2_img(data):
    buff = BytesIO(base64.b64decode(data))
    return Image.open(buff)


def handler(event, context):
    url = "https://unsplash.com/photos/E3LcqpQxtTU/download?force=true&w=640"
    response = requests.get(url)
  
    input_path = 'muh.jpg'
    output_path = 'output.png'

    input = Image.open(BytesIO(response.content))
    output = remove(input)
    #buffered = BytesIO()
    #output.save(buffered)
    
    im_b64 = im_2_b64(output)
    #print(im_b64)
    #img_str = base64.b64encode(buffered.getvalue())
    return {"content": im_b64.decode("utf-8")}