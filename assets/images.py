import requests
from PIL import Image
from io import BytesIO


# Returns image from url
def get_image(url_address):
    # Fetch the image using requests
    url = url_address
    response = requests.get(url)

    # If the request was successful, load and display the image
    if response.status_code == 200:
        img = Image.open(BytesIO(response.content))
        return img

