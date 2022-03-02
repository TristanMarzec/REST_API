
import flask
from types import NoneType

requestClientError = flask.Response(status=404)
requestServerError = flask.Response(status=500)
requestAccepted = flask.Response(status=200)

jsonFormat = "application/json"

methods = ['GET', 'POST', 'PUT', 'DELETE', 'PATCH', 'UPDATE', 'OPTIONS']


def check_object(data, object):
        if type(data) == NoneType:
            return False
        if object == data:
            return True
        if not len(data) == len(object):
            return False
        for key in object:
            if not type(data[key]) == type(object[key]):
                return False
        return True


class Request:
    def __init__(self, method: str, header: str, requestObject, responseObject):
        self.method = method
        self.header = header
        self.requestObject = requestObject
        self.responseObject = responseObject

    ### Getter and Setter ###

    def get_method(self):
        return self.methods
    
    def get_header(self):
        return self.header
    
    def get_request_object(self):
        return self.requestObject

    def get_response_object(self):
        return self.responseObject

    def set_method(self, methods):
        self.methods = methods

    def set_header(self, header):
        self.header = header
    
    def set_request_object(self, requestObject):
        self.requestObject = requestObject

    def set_response_Object(self, responseObject):
        self.responseObject = responseObject


    ### Methods ###

    def check_request(self, data):
        if not self.header["Content-Type"] == jsonFormat:
            return False
        if not check_object(data, self.get_request_object()):
            return False
        return True
    
    def check_response(self, data):
        if not check_object(data, self.get_response_object()):
            return False
        return True

    
    