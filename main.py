from flask import Flask, request, jsonify
import requests
import base64

app = Flask(__name__)

app_id = '680721238'

@app.route('/login', methods=['POST'])
def login():
    account_id = '7SBJ7GJKFJHXHGQU3G23U552NJZY5AQZO7NNVY76DFMDLWUPWZEIWH3NPQ'
    response = requests.get(f'https://testnet-idx.algonode.cloud/v2/accounts/{account_id}')
    data = response.json()
    address = data.get('account', {}).get('address', 'Không tìm thấy địa chỉ')
    return jsonify(account_address=address), 200

@app.route('/getAllBox', methods=['GET'])
def get_all_box():
    response = requests.get(f'https://testnet-idx.algonode.cloud/v2/applications/{app_id}/boxes')
    data = response.json()
    for box in data['boxes']:
        box['name'] = base64.b64decode(box['name']).decode('utf-8')
    return jsonify(data), 200
    
if __name__ == '__main__':
    app.run(debug=True)
