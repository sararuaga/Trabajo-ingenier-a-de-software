from flask import Flask, request, jsonify
from flask_cors import CORS
from flasgger import Swagger

app = Flask(__name__)
CORS(app)
swagger = Swagger(app)

# "Base de datos" en memoria
users = []

# CREATE - Registro de usuario
@app.route('/api/register', methods=['POST'])
def register():
    """
    Registro de usuario
    ---
    tags:
      - Usuarios
    parameters:
      - name: body
        in: body
        required: true
        schema:
          type: object
          properties:
            email:
              type: string
            password:
              type: string
            name:
              type: string
    responses:
      201:
        description: Usuario registrado
      400:
        description: Faltan datos
      409:
        description: Usuario ya existe
    """
    data = request.get_json()

    if not data or not data.get("email") or not data.get("password"):
        return jsonify({"error": "Email and password required"}), 400

    if any(u["email"] == data["email"] for u in users):
        return jsonify({"error": "User already exists"}), 409

    new_user = {
        "email": data["email"],
        "password": data["password"],
        "name": data.get("name", "")
    }
    users.append(new_user)

    return jsonify({"message": "User registered", "user": new_user}), 201


# READ - Login de usuario
@app.route('/api/login', methods=['POST'])
def login():
    """
    Login de usuario
    ---
    tags:
      - Usuarios
    parameters:
      - name: body
        in: body
        required: true
        schema:
          type: object
          properties:
            email:
              type: string
            password:
              type: string
    responses:
      200:
        description: Login exitoso
      400:
        description: Faltan datos
      401:
        description: Credenciales inválidas
    """
    data = request.get_json()

    if not data or not data.get("email") or not data.get("password"):
        return jsonify({"error": "Email and password required"}), 400

    user = next((u for u in users if u["email"] == data["email"] and u["password"] == data["password"]), None)

    if not user:
        return jsonify({"error": "Invalid credentials"}), 401

    return jsonify({"message": "Login successful", "user": user}), 200


if __name__ == '__main__':
    app.run(debug=True)
