from flask import Flask, request, jsonify, render_template

app = Flask(__name__)
users = []

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/users', methods=['POST'])
def add_user():
    data = request.get_json()
    required = ['name', 'email', 'phone', 'address']
    if not data or not all(field in data for field in required):
        return jsonify({'error': 'Missing user fields'}), 400

    users.append(data)
    return jsonify({'message': 'User added successfully'}), 201

@app.route('/users', methods=['GET'])
def get_users():
    return jsonify({'users': users})

if __name__ == '__main__':
    app.run(debug=True)
