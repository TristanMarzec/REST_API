import uuid

import models.list_model
from models.user_model import check_user





def check_existing_entry(listId, entryId):
     list = models.list_model.get_list(listId)
     if len(list["entries"]) == 0:
         return False
     for x in list["entries"]:
         if x["entryId"] == entryId:
             return True
        
def init_entry_by_id(listId, entryId):
    selectedList = models.list_model.get_list(listId)
    entry = get_entry(selectedList["entries"], entryId)
    entryToDelete = Entry(entry["name"], entry["content"], entry["userId"], listId)
    return entryToDelete

def init_entry_instance(data, listId):
    if not models.list_model.check_existing_list(listId):
        return
    author = data["userId"]
    if not check_user(author):
        return
    newEntry = Entry(data["name"], data["content"], author, listId)
    return newEntry

def init_change_entry_instance(data, listId, entryId):
    if models.list_model.check_existing_list(listId) and check_existing_entry(listId, entryId):
        entryToChange = Entry(data["name"], data["content"], data["userId"], listId)
        entryToChange.set_entry_id(entryId)
        return entryToChange

def get_entry(entries, id):
    for x in entries:
        if x["entryId"] == id:
            return x

class Entry:
    def __init__(self, name, content, user_id, list_id):
        self.entry_id = str(uuid.uuid4())
        self.name = name
        self.content = content
        self.user_id = user_id
        self.list_id = list_id
    
    ### Getter and Setter ###

    def set_entry_id(self, entry_id):
        self.entry_id = entry_id

    def set_name(self, name):
        self.name = name
    
    def set_content(self, content):
        self.content = content
    
    def set_user_id(self, user_id):
        self.user_id = user_id

    def set_list_id(self, list_id):
        self.list_id = list_id

    def get_entry_id(self):
        return self.entry_id

    def get_name(self):
        return self.name
    
    def get_content(self):
        return self.content
    
    def get_user_id(self):
        return self.user_id

    def get_list_id(self):
        return self.list_id

    ### Methods ###
    
    def entry_object_handler(self):
        entry = {
            "name": self.get_name(),
            "entryId": self.get_entry_id(),
            "content": self.get_content(),
            "userId": self.get_user_id(),
            "listId": self.get_list_id()
        }
        return entry

    def get_entry_from_list(self):
        specificList = models.list_model.get_list(self.get_list_id())
        for x in specificList["entries"]:
            if x["entryId"] == self.get_entry_id():
                return x

    def add_entry_to_list(self):
        if not check_user(self.get_user_id()):
            return
        inpList = models.list_model.get_list(self.get_list_id())
        inpList["entries"].append(self.entry_object_handler())
        newEntry = get_entry(inpList["entries"], self.get_entry_id())
        return newEntry

    def delete_entry_from_list(self):
        inpList = models.list_model.get_list(self.get_list_id())
        inpEntries = inpList["entries"]

        entryToDelete = self.entry_object_handler()
        print(inpList)
        print("--------------")
        print(inpEntries)
        print("--------------")
        
        inpEntries.remove(entryToDelete)
        
        return inpEntries

    def update_entry_from_list(self):
        inpList = models.list_model.get_list(self.get_list_id())
        inpEntries = inpList["entries"]

        oldEntry= self.get_entry_from_list()
        newEntry = self.entry_object_handler()

        inpEntries.remove(oldEntry)
        inpEntries.append(newEntry)

        updateEntry = get_entry(inpEntries, self.get_entry_id())
        return updateEntry


        

        



