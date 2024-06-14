from flask import Flask, jsonify
import requests

app = Flask(__name__)

@app.route('/login', methods=['POST'])
def login():
    account_id = '4AY36ICLI3G3CRFW2NZRDJGEKKT3YJFQL7JOSWVROWLVDT3N46YTHRCTLI'
    response = requests.get(f'http://localhost:8980/v2/accounts/{account_id}')
    data = response.json()
    address = data.get('account', {}).get('address', 'Không tìm thấy địa chỉ')
    return jsonify(account_address=address), 200
    
if __name__ == '__main__':
    app.run(debug=True)
