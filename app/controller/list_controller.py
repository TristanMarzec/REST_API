from crypt import methods
from flask import Blueprint, request


from models.list_model import init_list_instance, init_new_list, get_all_lists

from models.types import listBuilder, listResponse, listsBuilder
from models.request_model import Request, requestAccepted, requestClientError, requestServerError, methods


list_bp = Blueprint("list", __name__)

@list_bp.after_request
def apply_cors_header(response):
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['Access-Control-Allow-Methods'] = 'GET,POST,DELETE'
    response.headers['Access-Control-Allow-Headers'] = 'Content-Type'
    return response


@list_bp.route('/list/', methods=methods)
def endpoint_add_list():
    if not request.method == "POST":
        return requestServerError
    listRequest = Request('POST', request.headers, listBuilder, listResponse)
    data = request.get_json()
    if not listRequest.check_request(data):
        return requestServerError
    response = init_new_list(data)
    if not listRequest.check_response(response):
        return requestServerError
    return response
    
@list_bp.route('/lists/', methods=methods)
def endpoint_get_lists():
    if not request.method == 'GET':
        return requestServerError
    getListsRequest = Request('GET', request.headers, "", listsBuilder)
    if not getListsRequest.check_request(""):
        return requestClientError
    response = get_all_lists()
    if not getListsRequest.check_response(response):
        return requestClientError
    return response
    
    
    


@list_bp.route('/list/<string:list_id>/', methods=methods)
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
        deleteListRequest = Request("DELETE", request.headers, "", "")
        if not deleteListRequest.check_request(""):
            return requestClientError
        oldList = init_list_instance(list_id)
        if not deleteListRequest.check_response(""):
            return requestClientError
        oldList.remove_list()
        return requestAccepted
    else:
        return requestClientError



            