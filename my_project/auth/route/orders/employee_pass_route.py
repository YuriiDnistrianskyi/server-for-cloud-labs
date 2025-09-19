from http import HTTPStatus
from flask import Blueprint, jsonify, Response, request, make_response
from flask_jwt_extended import jwt_required
from my_project.auth.controller import employee_pass_controller
from my_project.auth.domain.orders.employee_pass import EmployeePass

employee_pass_bp = Blueprint('employee_pass', __name__, url_prefix='/employee_pass')

@employee_pass_bp.get('')
@jwt_required()
def get_all_employee_pass_bp() -> Response:
    employee_passes = employee_pass_controller.find_all()
    employee_pass_dto = [employee_pass.put_into_dto() for employee_pass in employee_passes]
    return make_response(jsonify(employee_pass_dto), HTTPStatus.OK)


@employee_pass_bp.post('')
@jwt_required()
def create_employee_pass() -> Response:
    data = request.get_json()
    employee_pass = EmployeePass.create_from_dto(data)
    employee_pass_controller.create_employee_pass(employee_pass)
    return make_response(jsonify(employee_pass.put_into_dto()), HTTPStatus.CREATED )


@employee_pass_bp.get('/<int:employee_pass_id>')
@jwt_required()
def get_employee_pass(employee_pass_id: int) -> Response:
    employee_pass = employee_pass_controller.find_employee_pass_by_id(employee_pass_id)
    return make_response(jsonify(employee_pass.put_into_dto()), HTTPStatus.OK)


@employee_pass_bp.put('/<int:employee_pass_id>')
@jwt_required()
def update_employee_pass(employee_pass_id: int) -> Response:
    data = request.get_json()
    employee_pass = EmployeePass.create_from_dto(data)
    employee_pass_controller.update_employee_pass(employee_pass_id, employee_pass)
    return make_response(jsonify({"message": "EmployeePass updated"}), HTTPStatus.OK)


@employee_pass_bp.delete('/<int:employee_pass_id>')
@jwt_required()
def delete_employee_pass(employee_pass_id: int) -> Response:
    employee_pass_controller.delete_employee_pass(employee_pass_id)
    return make_response(jsonify({"message": "EmployeePass deleted"}), HTTPStatus.OK)
