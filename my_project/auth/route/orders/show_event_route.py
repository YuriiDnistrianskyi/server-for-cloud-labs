from http import HTTPStatus
from flask import Blueprint, jsonify, Response, request, make_response
from flask_jwt_extended import jwt_required
from my_project.auth.controller import show_event_controller
from my_project.auth.domain.orders.show_event import ShowEvent

show_event_bp = Blueprint('show_event', __name__, url_prefix='/show_event')

@show_event_bp.get('')
@jwt_required()
def get_all_show_event() -> Response:
    show_events = show_event_controller.find_all()
    show_event_dto = [show_event.put_into_dto() for show_event in show_events]
    return make_response(jsonify(show_event_dto), HTTPStatus.OK)


@show_event_bp.post('')
@jwt_required()
def create_show_event() -> Response:
    data = request.get_json()
    show_event = ShowEvent.create_from_dto(data)
    show_event_controller.create_show_event(show_event)
    return make_response(jsonify(show_event.put_into_dto()), HTTPStatus.CREATED )


@show_event_bp.get('/<int:show_event_id>')
@jwt_required()
def get_show_event(show_event_id: int) -> Response:
    show_event = show_event_controller.find_show_event_by_id(show_event_id)
    return make_response(jsonify(show_event.put_into_dto()), HTTPStatus.OK)


@show_event_bp.put('/<int:show_event_id>')
@jwt_required()
def update_show_event(show_event_id: int) -> Response:
    data = request.get_json()
    show_event = ShowEvent.create_from_dto(data)
    show_event_controller.update_show_event(show_event_id, show_event)
    return make_response(jsonify({"message": "ShowEvent updated"}), HTTPStatus.OK)


@show_event_bp.delete('/<int:show_event_id>')
@jwt_required()
def delete_show_event(show_event_id: int) -> Response:
    show_event_controller.delete_show_event(show_event_id)
    return make_response(jsonify({"message": "ShowEvent deleted"}), HTTPStatus.OK)
