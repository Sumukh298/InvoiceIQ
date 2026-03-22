import re
import numpy as np
from flask import Flask, request, jsonify
import pytesseract
from PIL import Image
from flask_cors import CORS

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

app = Flask(__name__)
CORS(app)

@app.route('/')
def home():
    return "Server is running"

@app.route('/upload', methods=['POST'])
def upload():
    file = request.files['file']

    # 🖼️ Load + preprocess image
    img = Image.open(file)
    img = img.convert('L')  # grayscale

    # 🔥 Improve OCR accuracy
    img_np = np.array(img)
    img_np = (img_np > 150) * 255
    img = Image.fromarray(img_np.astype('uint8'))

    # 🧠 OCR
    text = pytesseract.image_to_string(img)

    # 🧹 Clean text
    clean_text = text.replace(" ", "").replace("\n", "")

    # ================= GSTIN =================
    gstin = "Not Found"

    lines = text.split('\n')

    for line in lines:
        if "gstin" in line.lower():
        # remove label
            possible = line.split(':')[-1].strip()

        # clean + normalize
            possible = possible.upper().replace('O', '0').replace('I', '1')

        # remove spaces
            possible = possible.replace(" ", "")

        # try to extract valid pattern
            match = re.search(r'\d{2}[A-Z]{5}\d{4}[A-Z0-9]{3}', possible)

            if match:
                gstin = match.group()
                break

    # ================= INVOICE NUMBER =================
    invoice_no = "Not Found"

    # Case 1: Invoice Number on same line
    match1 = re.search(
        r'Invoice\s*(No\.?|Number)\s*[:\-]?\s*([A-Z0-9\-]+)',
        text,
        re.IGNORECASE
    )

    # Case 2: Invoice Number on next line
    match2 = re.search(
        r'Invoice\s*(No\.?|Number)\s*\n+\s*([A-Z0-9\-]+)',
        text,
        re.IGNORECASE
    )

    if match1:
        invoice_no = match1.group(2)
    elif match2:
        invoice_no = match2.group(2)

    # ================= TOTAL =================
    total = "Not Found"
    numbers = re.findall(r'[\d,]+\.\d+', text)

    if numbers:
        total = max(numbers, key=lambda x: float(x.replace(',', '')))
    # ================= CONFIDENCE =================
    confidence = {
    "gstin": "Low",
    "invoice": "Low",
    "total": "Low"
    }

    if gstin != "Not Found":
        confidence["gstin"] = "High"

    if invoice_no != "Not Found":
        confidence["invoice"] = "High"

    if total != "Not Found":
        confidence["total"] = "High"
    

    return jsonify({
    "gstin": gstin,
    "invoice": invoice_no,
    "total": total,
    "confidence": confidence,
    "text": text
})

if __name__ == '__main__':
    app.run(debug=True)