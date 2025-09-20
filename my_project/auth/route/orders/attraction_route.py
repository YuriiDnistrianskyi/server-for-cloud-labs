from http import HTTPStatus
from flask import Blueprint, jsonify, Response, request, make_response
from flask_jwt_extended import jwt_required
from my_project.auth.controller import attraction_controller
from my_project.auth.domain.orders.attraction import Attraction

attraction_bp = Blueprint('attraction', __name__, url_prefix='/attraction')

@attraction_bp.get('')
@jwt_required()
def get_all_attractions() -> Response:
    """
        Get all attractions
        ---
        parameters:
          - name: Authorization
            in: header
            type: string
            required: true
            description: JWT token
            example: Bearer <token>
        responses:
            200:
              description: A list of attractions
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
                      example: Roller Coaster
                    capacity:
                      type: integer
                      example: 24
                    ticketBooking:
                       type: boolean
                       example: true
    """
    attractions = attraction_controller.find_all()
    attraction_dto = [attraction.put_into_dto() for attraction in attractions]
    return make_response(jsonify(attraction_dto), HTTPStatus.OK)


@attraction_bp.post('')
@jwt_required()
def create_attraction() -> Response:
    """
        Create a new attraction
        ---
        parameters:
          - name: Authorization
            in: header
            type: string
            required: true
            description: JWT token
            example: Bearer <token
          - name: body
            in: body
            required: true
            schema:
              type: object
              properties:
                name:
                  type: string
                  example: Attraction
                capacity:
                  type: integer
                  example: 40
                ticketBooking:
                  type: boolean
                  example: true
        responses:
          201:
            description: Attraction created successfully
            schema:
            type: object
            properties:
              id:
                type: integer
                example: 2
              name:
                type: string
                example: Attraction
              capacity:
                type: integer
                example: 40
              ticketBooking:
                type: boolean
                example: true
    """
    data = request.get_json()
    attraction = Attraction.create_from_dto(data)
    attraction_controller.create_attraction(attraction)
    return make_response(jsonify(attraction.put_into_dto()), HTTPStatus.CREATED )


@attraction_bp.get('/<int:attraction_id>')
@jwt_required()
def get_attraction(attraction_id: int) -> Response:
    """
        Get attraction by id
        ---
        parameters:
        - name: Authorization
          in: header
          type: string
          required: true
          description: JWT token
          example: Bearer <token>
        - name: attraction_id
          in: path
          type: integer
          required: true
          description: id of the attraction
          example: 1
        responses:
          200:
            description: Attraction found
            schema:
              type: object
              properties:
                id:
                  type: integer
                  example: 1
                name:
                  type: string
                  example: Attraction
                capacity:
                  type: integer
                  example: 24
                ticketBooking:
                  type: boolean
                  example: true
    """
    attraction = attraction_controller.find_attraction_by_id(attraction_id)
    return make_response(jsonify(attraction.put_into_dto()), HTTPStatus.OK)


@attraction_bp.put('/<int:attraction_id>')
@jwt_required()
def update_attraction(attraction_id: int) -> Response:
    """
        Update an existing attraction
        ---
        parameters:
        - name: Authorization
          in: header
          type: string
          required: true
          description: JWT token
          example: Bearer <token>
        - name: attraction_id
          in: path
          type: integer
          required: true
          description: id of the attraction to update
          example: 1
        - name: body
          in: body
          required: true
          schema:
            type: object
            properties:
              name:
                type: string
                example: Attraction
              capacity:
                type: integer
                example: 30
              ticketBooking:
                type: boolean
                example: false
        responses:
          200:
            description: Attraction updated successfully
            schema:
              type: object
              properties:
                message:
                  type: string
                  example: Attraction updated successfully
    """
    data = request.get_json()
    attraction = Attraction.create_from_dto(data)
    attraction_controller.update_attraction(attraction_id, attraction)
    return make_response(jsonify({"message": "Attraction updated"}), HTTPStatus.OK)


@attraction_bp.delete('/<int:attraction_id>')
@jwt_required()
def delete_attraction(attraction_id: int) -> Response:
    """
        Delete an attraction
        ---
        parameters:
        - name: Authorization
          in: header
          type: string
          required: true
          description: JWT token
          example: Bearer <token>
        - name: attraction_id
          in: path
          type: integer
          required: true
          description: id of the attraction to delete
          example: 1
        responses:
          200:
            description: Attraction deleted successfully
            schema:
              type: object
              properties:
                message:
                  type: string
                  example: Attraction deleted successfully
    """
    attraction_controller.delete_attraction(attraction_id)
    return make_response(jsonify({"message": "Attraction deleted"}), HTTPStatus.OK)


@attraction_bp.get('/name/<string:name>')
@jwt_required()
def get_attraction_by_name(name: str) -> Response:
    """
        Get attraction by name
        ---
        parameters:
            - name: Authorization
              in: header
              type: string
              required: true
              description: JWT token
              example: Bearer <token>
            - name: name
              in: path
              type: string
              required: true
              description: name of the attraction
              example: Attraction
        responses:
            200:
              description: Attraction found
              schema:
                type: array
                items:
                  type: object
                  properties:
                    id:
                      type: integer
                      example: 2
                    name:
                      type: string
                      example: Attraction
                    capacity:
                      type: integer
                      example: 40
                    ticketBooking:
                      type: boolean
                      example: true
    """
    attractions = attraction_controller.find_attraction_by_name(name)
    if attractions:
        return make_response(jsonify([attraction.put_into_dto() for attraction in attractions]), HTTPStatus.OK)
    return make_response(jsonify({"error": "Attractions not found"}), HTTPStatus.NOT_FOUND)


@attraction_bp.get('/capacity/<int:capacity>')
@jwt_required()
def get_attraction_by_capacity(capacity: int) -> Response:
    """
        Get attraction by capacity
        ---
        parameters:
            - name: Authorization
              in: header
              type: string
              required: true
              description: JWT token
              example: Bearer <token
            - name: capacity
              in: path
              type: integer
              required: true
              description: capacity of the attraction
              example: 40
        responses:
            200:
              description: Attraction found
              schema:
                type: array
                items:
                  type: object
                  properties:
                    id:
                      type: integer
                      example: 2
                    name:
                      type: string
                      example: Attraction
                    capacity:
                      type: integer
                      example: 40
                    ticketBooking:
                      type: boolean
                      example: true
    """
    attractions = attraction_controller.find_attraction_by_capacity(capacity)
    if attractions:
        return make_response(jsonify([attraction.put_into_dto() for attraction in attractions]), HTTPStatus.OK)
    return make_response(jsonify({"error": "Attractions not found"}), HTTPStatus.NOT_FOUND)
