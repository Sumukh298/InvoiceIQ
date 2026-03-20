from flask_cors import CORS
from flask import Flask, request, jsonify
import pytesseract
from PIL import Image

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

app = Flask(__name__)
CORS(app)
@app.route('/')
def home():
    return "Server is running"

@app.route('/upload', methods=['POST'])
def upload():
    file = request.files['file']
    img = Image.open(file)

    text = pytesseract.image_to_string(img)

    return jsonify({"text": text})

if __name__ == '__main__':
    print("Starting Flask...")
    app.run(debug=True)