# REST_API
In dieser Applikation wird eine REST-Schnittstelle zur Verfügung gestellt, um ToDo-Listen erstellen, bearbeiten und löschen zu können. Jede Liste besitzt einen Namen und Einträge. Mit diesen Einträgen kann genauso wie mit der Liste interagiert werden über die Schnittstelle. Zur eindeutigen Identifikation haben Listen und Einträge eine ID. Diese wird von der Schnittstelle generiert in einem UUID Format.
### [OpenAPI](https://swagger.io/specification/) Spezifikation wird verwendet

### [Python](https://www.python.org/) als Programmiersprache sowie [Flask](https://flask.palletsprojects.com/en/2.0.x/), um den Webserver aufsetzen zu können

## Hier ist die vordefinierte Spezifikation der Endpunkte zu sehen

<img width="868" alt="Bildschirmfoto 2022-02-02 um 13 37 06" src="https://user-images.githubusercontent.com/98464801/152155262-4bfd273e-df3c-4843-9152-cb15f16cffc4.png">


## Installation des Webservers
Über den pip package manager installieren Sie flask
```bash
pip install flask
````
oder
```bash
pip3 install flask
````
## Öffnen Sie nun ein Terminal/CMD im Projekt
```bash
cd app
````
Führen Sie dann den folgenden Command aus
```bash
flask run
````
### Die API ist unter der folgenden URL mit den jeweiligen Endpoints erreichbar
```https
url: "http://127.0.0.1:5000/"
createUser: "http://127.0.0.1:5000/user/"
allUsers: "http://127.0.0.1:5000/users/"
createList: "http://127.0.0.1:5000/list/"
getList/deleteList: "http://127.0.0.1:5000/list/{list_id}"
createEntry: "http://127.0.0.1:5000/list/{list_id}/entry"
getEntry/deleteEntry/changeEntry: "http://127.0.0.1:5000/list/{list_id}/entry/{entry_id}"
````

## Hier eine Auflistung der verschiedenen JSON-Objekte
Diese Objekte dienen zur Interaktion mit der API. Damit lassen sich ToDo-Listen erstellen, verändern, löschen sowie Einträge dort eingeben.
### User
```json
{
   "user": {
       "id": "string",
       "name": "string",
       "age": 0,
       "password": "string"
    }
    
}
````
### Liste mit einer ID, Name und Einträgen
```json
{
    "list": {
       "id": "string",
       "name": "string",
       "entries": []
    }
    
}
````
### Eintrag mit Eigenschaften und diversen ID's zur Identifikation
```json
{
   "entry": {
       "entryId": "string",
       "name": "string",
       "content": "string",
       "listId": "string",
       "userId": "string"
    }
    
}
````

