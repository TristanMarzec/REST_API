import uuid

import models.list_model
from models.user_model import check_user


def check_existing_entry(listId : str, entryId : str):
    """
    Diese Methode fragt ab ob ein Eintrag in der Liste existiert

    Parameters
    ----------
    listId : str, required
        ID der zu abfragenden Liste
    entryId : str, required
        ID des zu abfragenden Eintrags
    
    Returns
    -------
    True wenn der Eintrag existiert in der Liste
    False wenn die Liste leer ist oder der Eintrag nicht existiert
    """
    list = models.list_model.get_list(listId)
    if len(list["entries"]) == 0:
        return False
    for x in list["entries"]:
        if x["entryId"] == entryId:
            return True
    return False
        
def init_entry_by_id(listId : str, entryId : str):
    """
    Ein Eintrag wird neu Instanziert über die ID's

    Parameters
    ----------
    listId: str, required
        ID der zugehörigen Liste
    entryId: str, required
        ID des zu instanzierenden Eintrags
    
    Returns
    -------
    entryFromList als Variable des neu instanzierten Eintrags
    """
    selectedList = models.list_model.get_list(listId)
    entry = get_entry(selectedList["entries"], entryId)
    entryFromList = Entry(entry["name"], entry["content"], entry["userId"], listId)
    return entryFromList

def init_entry_instance(data, listId : str):
    """
    Ein neuer Eintrag für eine bestehende Liste wird instanziert

    Parameters
    ----------
    data : dict, required
        Die Daten für den neuen Eintrag werden als Parameter übergeben
    listId : str, required
        ID einer bestehenden Liste wird als Parameter übergeben
    
    Returns
    -------
    newEntry ist der neue Eintrag, welcher zurückgegeben wird
    """
    if not models.list_model.check_existing_list(listId):
        return
    author = data["userId"]
    if not check_user(author):
        return
    newEntry = Entry(data["name"], data["content"], author, listId)
    return newEntry

def init_change_entry_instance(data, listId : str, entryId : str):
    """
    Ein bestehender Eintrag wird durch diese Methode verändert

    Parameters
    ----------
    data : dict, required
        Daten für den neuen Eintrag
    listId : str, required
        ID der auszuwählenden Liste
    entryId : str, required
        ID des zu ändernden Eintrags
    
    Returns
    -------
    entryToChange gibt den veränderten Eintrag zurück
    """
    if models.list_model.check_existing_list(listId) and check_existing_entry(listId, entryId):
        entryToChange = Entry(data["name"], data["content"], data["userId"], listId)
        entryToChange.set_entry_id(entryId)
        return entryToChange

def get_entry(entries : list, id : str):
    """
    Gibt einen Eintrag aus einer bestimmten Liste zurück

    Parameters
    ----------
    entries : list, required
        Die Liste der Einträge
    id : str, required
        Die Id des zu abfragenden Eintrags
    """
    for x in entries:
        if x["entryId"] == id:
            return x

class Entry:
    """
    Die Entry Klasse definiert einen Eintrag einer Liste
    
    Attributes
    ---------
    name : str
        Der Name für den Eintrag
    content : str
        Der Inhalt des Eintrags
    user_id : str
        Die ID des Users, der den Eintrag erstellt hat.
    list_id : str
        Die ID der zugehörigen Liste
    """
    def __init__(self, name : str, content : str, user_id : str, list_id : str):
        """Contructor der Entry Klasse"""
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
        """Gibt ein Eintrags-Objekt zurück"""
        entry = {
            "name": self.get_name(),
            "entryId": self.get_entry_id(),
            "content": self.get_content(),
            "userId": self.get_user_id(),
            "listId": self.get_list_id()
        }
        return entry

    def get_entry_from_list(self):
        """
        
        """
        specificList = models.list_model.get_list(self.get_list_id())
        for x in specificList["entries"]:
            if x["entryId"] == self.get_entry_id():
                return x

    def add_entry_to_list(self):
        """
        Ein Eintrag wird zu einer Liste hinzugefügt

        Wenn die User ID invalide ist, kann der Eintrag nicht hinzugefügt werden

        Die Variable inpList definiert die zugehörige Liste

        Der Eintrag wird zur Liste hinzugefügt

        Zur Überprüfung wird der neue Eintrag aus der Liste aufgerufen mit der get_entry Methode
        """
        if not check_user(self.get_user_id()):
            return
        inpList = models.list_model.get_list(self.get_list_id())
        inpList["entries"].append(self.entry_object_handler())
        newEntry = get_entry(inpList["entries"], self.get_entry_id())
        return newEntry

    def delete_entry_from_list(self):
        """
        Ein Eintrag wird aus einer Liste gelöscht

        Die Variable inpList definiert die zugehörige Liste

        Über diese Variable wird die Variable inpEntries für alle Einträge dieser Liste definiert

        Der zu löschende Eintrag wird über die entry_object_handler Methode definiert

        Dann wird der Eintrag gelöscht und die Liste an Einträgen zurückgegeben
        """
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
        """
        Ein Eintrag einer Liste wird verändert
        
        Die Variable inpList definiert die zugehörige Liste

        Über diese Variable wird die Variable inpEntries für alle Einträge dieser Liste definiert

        Der alte Eintrag wird über die Methode get_entry_from_list aufgerufen
        Der neue Eintrag wird über die Methode entry_object_handler aufgerufen

        Der alte Eintrag wird entfernt und der neue hinzugefügt

        Dann wird der veränderte Eintrag aus der Liste aufgerufen und zurückgegeben
        """
        inpList = models.list_model.get_list(self.get_list_id())
        inpEntries = inpList["entries"]

        oldEntry= self.get_entry_from_list()
        newEntry = self.entry_object_handler()

        inpEntries.remove(oldEntry)
        inpEntries.append(newEntry)

        updateEntry = get_entry(inpEntries, self.get_entry_id())
        return updateEntry


        

        



