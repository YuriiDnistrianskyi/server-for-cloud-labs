from http import HTTPStatus
from flask import Blueprint, jsonify, Response, request, make_response
from flask_jwt_extended import jwt_required
from my_project.auth.controller import gender_controller
from my_project.auth.domain.orders.gender import Gender

gender_bp = Blueprint('gender', __name__, url_prefix='/gender')

@gender_bp.get('')
@jwt_required()
def get_all_genders() -> Response:
    genders = gender_controller.find_all()
    if not genders:
        return make_response(jsonify({"message": "None"}), HTTPStatus.NOT_FOUND)
    gender_dto = [gender.put_into_dto() for gender in genders]
    return make_response(jsonify(gender_dto), HTTPStatus.OK)


@gender_bp.post('')
@jwt_required()
def create_gender() -> Response:
    data = request.get_json()
    gender = Gender.create_from_dto(data)
    gender_controller.create_gender(gender)
    return make_response(jsonify(gender.put_into_dto()), HTTPStatus.CREATED )


@gender_bp.get('/<int:gender_id>')
@jwt_required()
def get_gender(gender_id: int) -> Response:
    gender = gender_controller.find_gender_by_id(gender_id)
    if gender:
        return make_response(jsonify(gender.put_into_dto()), HTTPStatus.OK)
    return make_response(jsonify({"error": "Gender not found"}), HTTPStatus.NOT_FOUND)


@gender_bp.put('/<int:gender_id>')
@jwt_required()
def update_gender(gender_id: int) -> Response:
    data = request.get_json()
    gender = Gender.create_from_dto(data)
    gender_controller.update_gender(gender_id, gender)
    return make_response(jsonify({"message": "Gender updated"}), HTTPStatus.OK)


@gender_bp.delete('/<int:gender_id>')
@jwt_required()
def delete_gender(gender_id: int) -> Response:
    gender_controller.delete_gender(gender_id)
    return make_response(jsonify({"message": "Gender deleted"}), HTTPStatus.OK)
