from io import BytesIO
from PIL import Image, ImageTk
import requests


def load_image_from_url(url, width, height):
    response = requests.get(url)
    img = Image.open(BytesIO(response.content))
    img = img.resize((width, height), Image.ANTIALIAS)
    return ImageTk.PhotoImage(img)
