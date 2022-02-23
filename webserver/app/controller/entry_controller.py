from flask import Blueprint, request

from models.entry_model import init_entry_instance, init_change_entry_instance, check_existing_entry, init_entry_by_id
from models.request_model import Request, requestAccepted, requestServerError, requestClientError
from models.types import entryBuilder, entryResponse


entry_bp = Blueprint("entry", __name__)


@entry_bp.route('/list/<string:list_id>/entry', methods=['POST'])
def endpoint_add_entry(list_id):
    addEntryRequest = Request("POST", request.headers, entryBuilder, entryResponse)
    data = request.get_json()
    if not addEntryRequest.check_request(data):
        return requestServerError
    inpEntry = init_entry_instance(data, list_id)
    if not inpEntry:
        return requestServerError
    response = inpEntry.add_entry_to_list()
    if not addEntryRequest.check_response(response):
        return requestServerError
    return response

@entry_bp.route('/list/<string:list_id>/entry/<string:entry_id>', methods=['POST', 'DELETE'])
def endpoint_entry(list_id, entry_id):
    if request.method == "POST":
        updateEntryRequest = Request("POST", request.headers, entryBuilder, entryResponse)
        data = request.get_json()
        if not updateEntryRequest.check_request(data):
            return requestClientError
        inpEntry = init_change_entry_instance(data, list_id, entry_id)
        response = inpEntry.update_entry_from_list()
        if not updateEntryRequest.check_response(response):
            return requestClientError
        return response
    elif request.method == "DELETE":
        deleteEntryRequest = Request("DELETE", request.headers, "", "")
        if not deleteEntryRequest.check_request(""):
            return requestClientError
        if not check_existing_entry(list_id, entry_id):
            return requestClientError
        entryDelete = init_entry_by_id(list_id, entry_id)
        entryDelete.delete_entry_from_list()
        if not deleteEntryRequest.check_response(""):
            return requestClientError
        return requestAccepted
