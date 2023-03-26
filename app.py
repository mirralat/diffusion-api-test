import base64
import io
import os

import requests
from PIL import PngImagePlugin, Image
from flask import Flask, send_file
from flask import render_template
import json
from dotenv import load_dotenv

load_dotenv()
URL = os.getenv('url')

app = Flask(__name__)


@app.route('/')
def index():
    print('home')
    return render_template('index.html')


@app.route('/set_data/<string:data>', methods=['POST'])
def process(data):
    print(data)
    data = json.loads(data)
    print("The string is", data)
    payload = {
        "prompt": data,
        "steps": 5
    }
    response = requests.post(url=f'{URL}/sdapi/v1/txt2img', json=payload)
    r = response.json()
    for i in r['images']:
        base = i.split(",", 1)[0]
        dt = base64.b64decode(base)
        image = Image.open(io.BytesIO(dt))

        png_payload = {
            "image": "data:image/png;base64," + i
        }
        response2 = requests.post(url=f'{URL}/sdapi/v1/png-info', json=png_payload)

        pnginfo = PngImagePlugin.PngInfo()
        pnginfo.add_text("parameters", response2.json().get("info"))
        image.save('output.png', pnginfo=pnginfo)
        return send_file('output.png', as_attachment=True)


if __name__ == '__main__':
    app.run(debug=True)
