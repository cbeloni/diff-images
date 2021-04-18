from flask import Flask, redirect, url_for, request
from flask import jsonify
import os
from werkzeug.utils import secure_filename

app = Flask(__name__)

ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}
todos = [{ "label": "My first task", "done": False }]

@app.route('/', methods=['GET'])
def home():
    return redirect(url_for('listar_todos'))

@app.route('/todos', methods=['GET'])
def listar_todos():
    json_text = jsonify(todos)        
    return json_text

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)