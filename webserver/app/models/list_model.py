
import uuid

from models.user_model import check_user
from models.types import entryBuilder
from models.entry_model import Entry
from models.request_model import check_object

lists = []


def lists_length():
    numOfLists = len(lists)
    return numOfLists

def check_existing_list(listId):
    if lists_length() == 0:
        return False
    for x in lists:
        if x["id"] == listId:
            return True
    return False

def get_list(listId):
    for x in lists:
        if x["id"] == listId:
            return x

def init_list_instance(listId):
    if check_existing_list(listId):
        data = get_list(listId)
        newList = List(data["name"], data["entries"], data["userId"])
        newList.set_id(listId)
        return newList

def init_new_list(data):
    author = data["userId"]
    if not check_user(author):
        return
    newList = List(data["name"], data["entries"], author)
    return newList.add_list()

class List:
    def __init__(self, listName, entries, userId):
        self.listName = listName
        self.entries = entries
        self.userId = userId
        self.id = str(uuid.uuid4())

    ### Getter and Setter ###

    def set_list_name(self, name):
        self.listName = name
    
    def set_entries(self, entries):
        self.entries = entries
    
    def set_id(self, id):
        self.id = id

    def set_user_id(self, userId):
        self.userId = userId

    def get_list_name(self):
        return self.listName
    
    def get_entries(self):
        return self.entries

    def get_id(self):
        return self.id
    
    def get_user_id(self):
        return self.userId

    def get_list_object(self):
        listObject = {
            "id": self.get_id(),
            "name": self.get_list_name(),
            "entries": self.get_entries(),
            "userId": self.get_user_id(),
        }
        return listObject

    ### Methods ###
    
    def add_list(self):
        self.set_entries(self.check_for_entries())
        listToAdd = self.get_list_object()
        lists.append(listToAdd)
        return listToAdd
    
    def remove_list(self):
        listToRemove = self.get_list_object()
        lists.remove(listToRemove)
        return lists
    
    def check_for_entries(self):
        entries = self.get_entries()
        entryList = len(entries)
        newEntryList = []
        if len(entries) == 0:
            return []
        for i in range(entryList):
            entry = entries[i]
            if not check_object(entry, entryBuilder):
                return []
            newEntry = Entry(entry["name"], entry["content"], self.get_user_id(), self.get_id())
            newEntryList.append(newEntry.entry_object_handler())
        return newEntryList
            
        
                



