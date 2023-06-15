
import openai
from config import chatgpt_api_key

import requests
async def generate_img(prompt):
    openai.api_key = chatgpt_api_key
    #print('Write your prompt: ')

    model = "image-alpha-001"
    response_format = "url"
    #print('Write number of pictures: ')


    # make the API request
    response = openai.Image.create(prompt=prompt, model=model, response_format=response_format, n=1)
    image_url = response["data"][0]["url"]
    response = requests.get(image_url)
    return(image_url)