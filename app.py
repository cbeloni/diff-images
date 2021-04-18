from flask import Flask, redirect, url_for, request
from flask import jsonify
from src import CompareImage
import os
from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return "<h1>Hello World</hi>"

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

#separar envio de imagem e comparador de imagem

@app.route('/diff', methods=['POST'])
def comparar_imagem():
    file = request.files['file']
    filediff = request.files['filediff']
    dir_root = os.path.dirname(os.path.abspath(__file__))
    image_difference = 100
    UPLOAD_DIR = dir_root + "/src/files/"
    if file and allowed_file(file.filename) and filediff and allowed_file(filediff.filename):
        filename = secure_filename(file.filename)
        filename_diff = secure_filename(filediff.filename)
        file.save(os.path.join(UPLOAD_DIR, filename))
        filediff.save(os.path.join(UPLOAD_DIR, filename_diff))
        compare_image = CompareImage(UPLOAD_DIR + filename, UPLOAD_DIR + filename_diff)
        image_difference = compare_image.compare_image()

    print (image_difference)
    return str(image_difference)

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=True)
