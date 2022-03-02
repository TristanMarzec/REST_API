from flask import Flask

from controller.list_controller import list_bp
from controller.user_controller import user_bp
from controller.entry_controller import entry_bp

app = Flask(__name__)


app.register_blueprint(list_bp)
app.register_blueprint(user_bp)
app.register_blueprint(entry_bp)

@app.route("/")
def default():
    return "<h1>Dies ist die ToDo-Listen API</h1>"

if __name__ == '__main__':
    app.run(host='127.0.0.1', port='5000')