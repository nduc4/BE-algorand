from flask import Flask, request, jsonify
import requests
import base64

app = Flask(__name__)

BASE_URL = 'https://testnet-idx.algonode.cloud/v2'
APP_ID = '680721238'
ACCOUNT_ID = '7SBJ7GJKFJHXHGQU3G23U552NJZY5AQZO7NNVY76DFMDLWUPWZEIWH3NPQ'

def decode_base64(data):
    return base64.b64decode(data.encode()).decode()

@app.route('/login', methods=['POST'])
def login():
    response = requests.get(f'{BASE_URL}/accounts/{ACCOUNT_ID}')
    data = response.json()
    address = data.get('account', {}).get('address', 'Không tìm thấy địa chỉ')
    return jsonify(account_address=address), 200

@app.route('/getAllBox', methods=['GET'])
def get_all_box():
    response = requests.get(f'{BASE_URL}/applications/{APP_ID}/boxes')
    data = response.json()
    for box in data['boxes']:
        box['name'] = decode_base64(box['name'])
    return jsonify(data), 200

@app.route('/getDetailsBox', methods=['GET'])
def get_details_box():
    name = request.args.get('name', default = None, type = str)
    name_encoded = base64.b64encode(name.encode()).decode()
    response = requests.get(
        f'{BASE_URL}/applications/{APP_ID}/box',
        params={'name': 'b64:' + name_encoded}
    )
    data = response.json()
    for key in data:
        if isinstance(data[key], str):
            try:
                data[key] = decode_base64(data[key])
            except ValueError:
                pass
    return jsonify(data), 200
    
if __name__ == '__main__':
    app.run(debug=True)
