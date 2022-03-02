import uuid



users = {
    "userList": []
}

def users_length():
    numOfUsers = len(users["userList"])
    return numOfUsers

def check_user(userId):
    if len(userId) == 0 or not userId:
        return False
    for x in users["userList"]:
        if x["id"] == userId:
            return True
    return False

def init_user_instance(userId):
    data = get_user(userId)
    newUser = User(data["name"], data["age"], data["password"])
    newUser.set_id(userId)
    return newUser

def get_all_users():
       return users

def get_user(id):
    for x in users["userList"]:
        if x["id"] == id:
            return x



class User:

    def __init__(self, name: str, age: int, password: str):
        self.name = name
        self.age = age
        self.password = password
        self.id = str(uuid.uuid4())
    
    ### Getter and Setter ###

    def set_name(self, name):
        self.name = name
    
    def set_age(self, age):
        self.age = age
    
    def set_password(self, password):
        self.password = password
    
    def set_id(self, id):
        self.id = id
    
    def get_name(self):
        return self.name
    
    def get_age(self):
        return self.age

    def get_password(self):
        return self.password

    def get_id(self):
        return self.id
    ### Methods ###

    def delete_user(self):
        if not check_user(self.get_id()):
            return False
        userToDelete = get_user(self.get_id())
        users["userList"].remove(userToDelete)
        return True
    
    def add_user(self):
        userToAdd = {
            "name": self.get_name(),
            "age": self.get_age(),
            "password": self.get_password(),
            "id": self.get_id()
        }
        users["userList"].append(userToAdd)
        if not check_user(self.get_id()):
            return False
        return userToAdd