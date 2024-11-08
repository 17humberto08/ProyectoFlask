from flask import Flask
from myapp.config import DevConfig
from myapp.task.controllers import taskRoute

app = Flask(__name__)
app.register_blueprint(taskRoute)
app.config.from_object(DevConfig)

@app.route('/')
def hello_world() -> str:
    return 'hello world'
