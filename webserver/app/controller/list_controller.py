from flask import Blueprint, request


from models.list_model import init_list_instance, init_new_list

from models.types import listBuilder, listResponse
from models.request_model import Request, requestAccepted, requestClientError, requestServerError


list_bp = Blueprint("list", __name__)

### Defining all List routes for requests ###

@list_bp.route('/list/', methods=['POST'])
def endpoint_add_list():
    if request.method != "POST":
        return requestServerError
    listRequest = Request('POST', request.headers, listBuilder, listResponse)
    data = request.get_json()
    if not listRequest.check_request(data):
        return requestServerError
    response = init_new_list(data)
    if not listRequest.check_response(response):
        return requestServerError
    return response
    



@list_bp.route('/list/<string:list_id>/', methods=['GET', 'DELETE'])
def endpoint_list(list_id):
    if request.method == "GET":
        getListRequest = Request("GET", request.headers, "", listResponse)
        if not getListRequest.check_request(""):
            return requestClientError
        initList = init_list_instance(list_id)
        newList = initList.get_list_object()
        if not getListRequest.check_response(newList):
            return requestClientError
        return newList
    elif request.method == "DELETE":
        deleteListRequest = Request("DELETE", "", "")
        if not deleteListRequest.check_request(""):
            return requestClientError
        oldList = init_list_instance(list_id)
        if not deleteListRequest.check_response(""):
            return requestClientError
        oldList.remove_list()
        return requestAccepted



            