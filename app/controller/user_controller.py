from flask import Blueprint, request


from models.request_model import Request, requestAccepted, requestClientError, requestServerError, methods
from models.user_model import User, init_user_instance, get_all_users
from models.types import userBuilder, userListBuilder, userResponse


user_bp = Blueprint("user", __name__)

@user_bp.after_request
def apply_cors_header(response):
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['Access-Control-Allow-Methods'] = 'GET,POST,DELETE'
    response.headers['Access-Control-Allow-Headers'] = 'Content-Type'
    return response




@user_bp.route('/users/', methods=methods)
def endpoint_get_all_users():
    if not request.method == 'GET':
        return requestClientError
    allUserRequest = Request("GET", request.headers, "", userListBuilder)
    if not allUserRequest.check_request(""):
        return requestServerError
    response = get_all_users()
    if not allUserRequest.check_response(response):
        return requestServerError
    return response
        

@user_bp.route('/user/', methods=methods)
def endpoint_add_user():
    if not request.method == 'POST':
        return requestClientError
    addUserRequest = Request("POST", request.headers, userBuilder, userResponse)
    data = request.get_json()
    if not addUserRequest.check_request(data):
        return requestServerError
    newUser = User(data["name"], data["age"], data["password"])
    response = newUser.add_user()
    if not addUserRequest.check_response(response):
        return requestServerError
    return response

@user_bp.route('/user/<string:user_id>/', methods=methods)
def endpoint_delete_user(user_id):
    if not request.method == 'DELETE':
        return requestClientError
    deleteUserRequest = Request("DELETE", request.headers, "", "")
    if not deleteUserRequest.check_request(""):
        return requestClientError
    userDelete = init_user_instance(user_id)
    if not userDelete.delete_user():
        return requestClientError
    if not deleteUserRequest.check_response(""):
        return requestClientError
    return requestAccepted