import shutil
import os
from flask import Flask, render_template, request, redirect, jsonify, send_from_directory
from PyPDF2 import PdfReader, PdfWriter
from pathlib import Path

app = Flask(__name__)

UPLOAD_FOLDER = 'uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/split/<path:path>')
def send_report(path):
    return send_from_directory('split', path)


@app.route('/merge/<path:path>')
def send_merge(path):
    return send_from_directory('merge', path)


@app.route('/split_to_zip', methods=['POST'])
def split_to_zip():
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
        with open(filename, 'rb') as pdf_file:
            pdf_reader = PdfReader(pdf_file)
            num_pages = len(pdf_reader.pages)
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


@app.route('/merge_to_pdf', methods=['POST'])
def merge_to_pdf():
    if 'pdf_1' not in request.files or 'pdf_2' not in request.files:
        return redirect(request.url)

    pdf_file_1 = request.files['pdf_1']
    pdf_file_2 = request.files['pdf_2']

    if pdf_file_1.filename == '' or pdf_file_2.filename == '':
        return redirect(request.url)

    if pdf_file_1:
        filename_1 = os.path.join(app.config['UPLOAD_FOLDER'], pdf_file_1.filename)
        pdf_file_1.save(filename_1)

    if pdf_file_2:
        filename_2 = os.path.join(app.config['UPLOAD_FOLDER'], pdf_file_2.filename)
        pdf_file_2.save(filename_2)

    if pdf_file_1 and pdf_file_2:

        with open(filename_1, 'rb') as pdf_file_1, open(filename_2, 'rb') as pdf_file_2:
            pdf_reader_1 = PdfReader(pdf_file_1)
            pdf_reader_2 = PdfReader(pdf_file_2)

            Path("/tmp/merge_pdf").mkdir(parents=True, exist_ok=True)
            writer = PdfWriter()

            for page_num in range(len(pdf_reader_1.pages)):
                writer.add_page(pdf_reader_1.pages[page_num])

            for page_num in range(len(pdf_reader_2.pages)):
                writer.add_page(pdf_reader_2.pages[page_num])

            out_filename = '/app/merge/merger.pdf'
            with open(out_filename, 'wb') as outfile:
                writer.write(outfile)

            response = jsonify({"url": '/merge/merger.pdf', "name": 'merge.pdf'})
            # response.headers.add("Access-Control-Allow-Origin", "*")
            return response


if __name__ == '__main__':

    app.run(debug=True)
