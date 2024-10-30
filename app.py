from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello, World!"


@app.route('/api/<id>', methods=['GET'])
def get_content(id):    
    if id == '1':
        response = {
            "message": "ini konten dengan id " + id,
        }
        return jsonify(response), 200 
    else:
        response = {
            "message": "Ini bukan konten dengan id 1",
        }
        return jsonify(response), 200

# Endpoint untuk menerima data POST
@app.route('/login', methods=['POST'])
def login():
    # Mengambil data JSON dari permintaan
    data = request.get_json()
    
    if not data or 'username' not in data or 'password' not in data:    
        return jsonify({"error": "invalid syntax"}), 400

    # Simpan atau proses data sesuai kebutuhan
    username = data['username']
    password = data['password']

    valid_username = 'undiksha'
    valid_password = 'admin#1234'

    if username == valid_username and password == valid_password:    
        response = {
            "message": "Selamat kamu berhasil login!",
            "received_data": {
                "username": username,
            }
        }
        
        return jsonify(response), 201 # 201: Created
    else:
        return jsonify({"error": "username atau password salah"}), 401

if __name__ == '__main__':
    app.run(debug=True)