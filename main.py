from flask import Flask, request
import requests

app = Flask(__name__)


@app.route('/')
def index():

    print(request.remote_addr)

    # url = f"http://api.ipstack.com/{request.remote_addr}"

    # params={'access_key': '92a42fef93ee5935cc68c86ed0c3bc38'}

    # req = requests.get(url, params=params)

    # print(req.json())

    return f'{request.remote_addr}!'


app.run(host='0.0.0.0', port=81)
