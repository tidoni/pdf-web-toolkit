from flask import Flask, render_template, request, redirect, url_for, jsonify, send_from_directory
import os
from PyPDF2 import PdfReader, PdfWriter

from pathlib import Path
import shutil
import os

app = Flask(__name__)

UPLOAD_FOLDER = 'uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/split/<path:path>')
def send_report(path):
    return send_from_directory('split', path)

@app.route('/split', methods=['POST'])
def split_file():
    if 'pdf' not in request.files:
        return redirect(request.url)

    pdf_file = request.files['pdf']

    if pdf_file.filename == '':
        return redirect(request.url)

    if pdf_file:
        in_filename = pdf_file.filename
        filename = os.path.join(app.config['UPLOAD_FOLDER'], pdf_file.filename)
        pdf_file.save(filename)
        

        out_filenames = []
        Path("/tmp/split_pdf").mkdir(parents=True, exist_ok=True)
        # Process the PDF file (e.g., extract text)
        with open(filename, 'rb') as pdf_file:
            pdf_reader = PdfReader(pdf_file)
            num_pages = len(pdf_reader.pages)
            text = ''
            for page_num in range(num_pages):

                writer = PdfWriter()
                writer.add_page(pdf_reader.pages[page_num])

                out_filename = '/tmp/split_pdf/' + in_filename + '_' + str(page_num) + '.pdf'
                with open(out_filename, 'wb') as outfile:
                    writer.write(outfile)
                    out_filenames.append(out_filename)

        shutil.make_archive(in_filename.rsplit('.', 1)[0] + '_splitted', 'zip', "/tmp/split_pdf")
        zip_filename = in_filename.rsplit('.', 1)[0] + "_splitted.zip"
        os.rename("/app/" + zip_filename, "/app/split/" + zip_filename)

        for temp_file in out_filenames:
            Path.unlink(temp_file)

        response = jsonify({"url": "/split/" + zip_filename, "name": zip_filename})
        # response.headers.add("Access-Control-Allow-Origin", "*")
        return response

if __name__ == '__main__':
    app.run(debug=True)
