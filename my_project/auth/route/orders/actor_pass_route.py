from http import HTTPStatus
from flask import Blueprint, jsonify, Response, request, make_response
from flask_jwt_extended import jwt_required
from my_project.auth.controller import actor_pass_controller
from my_project.auth.domain.orders.actor_pass import ActorPass

actor_pass_bp = Blueprint('ActorPass', __name__, url_prefix='/actor_pass')

@actor_pass_bp.get('')
@jwt_required()
def get_all_actor_pass() -> Response:
    actor_passes = actor_pass_controller.find_all()
    attraction_dto = [actor_pass.put_into_dto() for actor_pass in actor_passes]
    return make_response(jsonify(attraction_dto), HTTPStatus.OK)


@actor_pass_bp.post('')
def create_actor_pass() -> Response:
    data = request.get_json()
    actor_pass = ActorPass.create_from_dto(data) #
    actor_pass_controller.create_actor_pass(actor_pass)
    return make_response(jsonify(actor_pass.put_into_dto()), HTTPStatus.CREATED )


@actor_pass_bp.get('/<int:actor_pass_id>')
@jwt_required()
def get_actor_pass(actor_pass_id: int) -> Response:
    actor_pass = actor_pass_controller.find_actor_pass_by_id(actor_pass_id)
    return make_response(jsonify(actor_pass.put_into_dto()), HTTPStatus.OK)


@actor_pass_bp.put('/<int:actor_pass_id>')
@jwt_required()
def update_attraction(actor_pass_id: int) -> Response:
    data = request.get_json()
    actor_pass = ActorPass.create_from_dto(data) #
    actor_pass_controller.update_actor_pass(actor_pass_id, actor_pass)
    return make_response(jsonify({"message": "ActorPass updated"}), HTTPStatus.OK)


@actor_pass_bp.delete('/<int:actor_pass_id>')
@jwt_required()
def delete_actor_pass(actor_pass_id: int) -> Response:
    actor_pass_controller.delete_actor_pass(actor_pass_id)
    return make_response(jsonify({"message": "ActorPass deleted"}), HTTPStatus.OK)
