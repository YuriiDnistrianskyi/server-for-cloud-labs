from http import HTTPStatus
from flask_jwt_extended import create_access_token
from flask import Blueprint, request, Response, make_response, jsonify
from my_project.auth.domain.orders.Park import Park

auth_bp = Blueprint('auth', __name__, url_prefix='/auth')

@auth_bp.post("/login")
def login() -> Response:
    """
        Login
        ---
        parameters:
        - name: body
          in: body
          required: true
          schema:
            type: object
            properties:
              name:
                type: string
                example: "Park"
              password:
                type: string
                example: "password123"
        responses:
          200:
            description: Login successful
            schema:
              type: object
              properties:
                access_token:
                  type: string
                  example: "<access_token>"
    """
    data = request.get_json()
    park = Park.query.filter_by(name=data["name"]).first()
    if park is not None and park.password == data['password']:
        access_token = create_access_token(identity=str(park.id))
        return make_response(jsonify({'access_token': access_token}), HTTPStatus.OK)

    return make_response(jsonify({"message": f"Not found Park {data['name']} or bad password"}), HTTPStatus.NOT_FOUND)
