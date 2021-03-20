from flask import Flask, redirect, url_for
from flask import jsonify
from src import CompareImage

app = Flask(__name__)

todos = [{ "label": "My first task", "done": False }]

@app.route('/', methods=['GET'])
def home():
    return redirect(url_for('listar_todos'))

@app.route('/todos', methods=['GET'])
def listar_todos():
    json_text = jsonify(todos)        
    return json_text

@app.route('/diff', methods=['GET'])    
def comparar_imagem():
    compare_image = CompareImage('baby_yoda1.jpg', 'baby_yoda1.jpg')
    image_difference = compare_image.compare_image()
    print (image_difference)
    return str(image_difference)

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=True)