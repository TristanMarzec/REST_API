from flask import Blueprint, request


from models.request_model import Request, requestAccepted, requestClientError, requestServerError
from models.user_model import User, init_user_instance, get_all_users
from models.types import userBuilder, userListBuilder, userResponse


user_bp = Blueprint("user", __name__)


### Defining all user routes for requests ###



@user_bp.route('/users/', methods=['GET'])
def endpoint_get_all_users():
    allUserRequest = Request("GET", request.headers, "", userListBuilder)
    if not allUserRequest.check_request(""):
        return requestServerError
    response = get_all_users()
    if not allUserRequest.check_response(response):
        return requestServerError
    return response
        

@user_bp.route('/user/', methods=['POST'])
def endpoint_add_user():
    addUserRequest = Request("POST", request.headers, userBuilder, userResponse)
    data = request.get_json()
    if not addUserRequest.check_request(data):
        return requestServerError
    newUser = User(data["name"], data["age"], data["password"])
    response = newUser.add_user()
    if not addUserRequest.check_response(response):
        return requestServerError
    return response

@user_bp.route('/user/<string:user_id>/', methods=['DELETE'])
def endpoint_delete_user(user_id):
    deleteUserRequest = Request("DELETE", request.headers, "", "")
    if not deleteUserRequest.check_request(""):
        return requestClientError
    userDelete = init_user_instance(user_id)
    if not userDelete.delete_user():
        return requestClientError
    if not deleteUserRequest.check_response(""):
        return requestClientError
    return requestAccepted