from http import HTTPStatus
from flask import Blueprint, jsonify, Response, request, make_response
from flask_jwt_extended import jwt_required
from my_project.auth.controller import park_controller
from my_project.auth.domain.orders.Park import Park

park_bp = Blueprint('park', __name__, url_prefix='/park')

@park_bp.get('')
@jwt_required()
def get_all_parks() -> Response:
    """
        Get All Parks
        ---
        parameters:
          - name: Authorization
            in: header
            type: string
            required: true
            description: JWT token
            example: "Bearer <your_jwt_token>"
        responses:
          200:
            description: A list of parks
            schema:
              type: array
              items:
                type: object
                properties:
                  id:
                    type: integer
                    example: 1
                  name:
                    type: string
                    example: "Park"
                  password:
                    type: number
                    example: 1111
                  location:
                    type: string
                    example: "Lviv"
                  maxVisit:
                    type: number
                    example: 100
                  attractionNumber:
                    type: number
                    example: 1000
                  age:
                    type: number
                    example: 5
    """
    park = park_controller.find_all()
    park_dto = [park.put_into_dto() for park in park]
    return make_response(jsonify(park_dto), HTTPStatus.OK)


@park_bp.post('')
def create_park() -> Response:
    """
        Create Park
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
                  type: number
                  example: 1111
                location:
                  type: string
                  example: "Lviv"
                maxVisit:
                  type: number
                  example: 100
                attractionNumber:
                   type: number
                   example: 1000
                age:
                   type: number
                   example: 5
        responses:
          201:
            description: Park created
            schema:
              type: object
              properties:
                name:
                  type: string
                  example: "Park"
                password:
                  type: number
                  example: 1111
                location:
                  type: string
                  example: "Lviv"
                maxVisit:
                  type: number
                  example: 100
                attractionNumber:
                   type: number
                   example: 1000
                age:
                   type: number
                   example: 5
        """
    data = request.get_json()
    park = Park.create_from_dto(data)
    park_controller.create_park(park)
    return make_response(jsonify(park.put_into_dto()), HTTPStatus.CREATED)


@park_bp.post('/params')
@jwt_required()
def create_by_params() -> Response:
    """
        Create Park by params
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
                  type: number
                  example: 1111
                location:
                  type: string
                  example: "Lviv"
                maxVisit:
                  type: number
                  example: 100
                attractionNumber:
                   type: number
                   example: 1000
                age:
                    type: number
                    example: 5
        responses:
          200:
            description: Park created by params
            schema:
              type: object
              properties:
                message:
                  type: string
                  example: "Created park by parms"
    """
    data = request.get_json()
    park_controller.create_by_params(data)
    return make_response(jsonify({"message": "Created park by parms"}), HTTPStatus.OK)


@park_bp.get('/<int:park_id>')
@jwt_required()
def get_park(park_id: int) -> Response:
    """
        Get Park by ID
        ---
        parameters:
          - name: Authorization
            in: header
            type: string
            required: true
            description: JWT token
            example: "Bearer <your_jwt_token>"
          - name: park_id
            in: path
            required: true
            type: integer
            example: 1
        responses:
          200:
            description: Park found
            schema:
              type: object
              properties:
                id:
                  type: integer
                  example: 1
                name:
                  type: string
                  example: "Park"
                password:
                  type: number  
                  example: 1111
                location:
                  type: string
                  example: "Lviv"
                maxVisit:
                  type: number
                  example: 100
                attractionNumber:
                  type: number
                  example: 1000
                age:
                    type: number
                    example: 5
    """
    park = park_controller.find_by_id(park_id)
    if park:
        return make_response(jsonify(park.put_into_dto()), HTTPStatus.OK)
    return make_response(jsonify({"error": "Park not found"}), HTTPStatus.NOT_FOUND)


@park_bp.put('/<int:park_id>')
@jwt_required()
def update_park(park_id: int) -> Response:
    """
        Update Park
        ---
        parameters:
          - name: Authorization
            in: header
            type: string
            required: true
            description: JWT token
            example: "Bearer <your_jwt_token>"
          - name: park_id
            in: path
            required: true
            type: integer
            example: 1
          - name: body
            in: body
            required: true
            schema:
              type: object
              properties:
                name:
                  type: string
                  example: "Updated Park"
                password:
                  type: number
                  example: 2222
                location:
                  type: string
                  example: "Kyiv"
                maxVisit:
                  type: number
                  example: 200
                attractionNumber:
                  type: number
                  example: 2000
                age:
                  type: number
                  example: 10
        responses:
          200:
            description: Park updated
            schema:
              type: object
              properties:
                message:
                  type: string
                  example: "Park updated"
    """
    data = request.get_json()
    park = Park.create_from_dto(data)
    park_controller.update_park(park_id, park)
    return make_response(jsonify({"messange": "Park updated"}), HTTPStatus.OK)


@park_bp.delete('/<int:park_id>')
@jwt_required()
def delete_park(park_id: int) -> Response:
    """
      Delete Park
      ---
      parameters:
        - name: Authorization
          in: header
          type: string
          required: true
          description: JWT token
          example: "Bearer <your_jwt_token>"
        - name: park_id
          in: path
          required: true
          type: integer
          example: 1
      responses:
        200:
          description: Park deleted
          schema:
            type: object
            properties:
              message:
                type: string
                example: "Park deleted"
    """
    park_controller.delete_park(park_id)
    return make_response(jsonify({"messange": "Park deleted"}), HTTPStatus.OK)

@park_bp.get('/name/<string:name>')
@jwt_required()
def get_park_by_name(name: str) -> Response:
    """
        Get Park by Name
        ---
        parameters:
          - name: Authorization
            in: header
            type: string
            required: true
            description: JWT token
            example: "Bearer <your_jwt_token>"
          - name: name
            in: path
            required: true
            type: string
            example: "Park"
        responses:
          200:
            description: Park found
            schema:
              type: array
              items:
                properties:
                    name:
                      type: string
                      example: "Park"
                    password:
                      type: number
                      example: 1111
                    location:
                      type: string
                      example: "Lviv"
                    maxVisit:
                      type: number
                      example: 100
                    attractionNumber:
                      type: number
                      example: 1000
                    age:
                      type: number
                      example: 5
    """
    parks = park_controller.find_by_name(name)
    if parks:
        return make_response(jsonify([park.put_into_dto() for park in parks]), HTTPStatus.OK)
    return make_response(jsonify({"error": "Park not found"}), HTTPStatus.NOT_FOUND)

@park_bp.get('/location/<string:location>')
@jwt_required()
def get_park_by_location(location: str) -> Response:
    """
        Get Park by Location
        ---
        parameters:
          - name: Authorization
            in: header
            type: string
            required: true
            description: JWT token
            example: "Bearer <your_jwt_token>"
          - name: location
            in: path
            required: true
            type: string
            example: "Lviv"
        responses:
          200:
            description: Park found
            schema:
              type: array
              items:
                properties:
                    name:
                      type: string
                      example: "Park"
                    password:
                      type: number
                      example: 1111
                    location:
                      type: string
                      example: "Lviv"
                    maxVisit:
                      type: number
                      example: 100
                    attractionNumber:
                      type: number
                      example: 1000
                    age:
                      type: number
                      example: 5
    """
    parks = park_controller.find_by_location(location)
    if parks:
        return make_response(jsonify([park.put_into_dto() for park in parks]), HTTPStatus.OK)
    return make_response(jsonify({"error": "Park not found"}), HTTPStatus.NOT_FOUND)
