import requests
import os
from datetime import datetime
from PIL import Image, ImageDraw, ImageFont
from dotenv import load_dotenv

load_dotenv()

username = "${{ github.repository_owner }}" # Seu username do GitHub
date_since = os.getenv('SINCE') or '00000000'
api_url = f'https://github.com/users/{username}/contributions?from={date_since}'
response = requests.get(api_url)
if response.status_code == 200:
    with open("snake.svg", "wb") as f:
        f.write(response.content)

img = Image.new('RGB', (1280, 720), color = (255, 255, 255))
font = ImageFont.truetype('arial.ttf', 30)
d = ImageDraw.Draw(img)
d.text((10, 10), "Hello, World!", font=font, fill=(0, 0, 0))
img.save('dist/test.png')

os.system('git config --global user.email "<seu-email>"')
os.system('git config --global user.name "<seu-username>"')
os.system('git add .')
os.system('git commit -m "Update snake image"')
os.system('git push origin master')
