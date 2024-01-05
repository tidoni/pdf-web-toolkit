import shutil
import os
from flask import Flask, render_template, request, redirect, jsonify, send_from_directory
from pypdf import PdfReader, PdfWriter
from pathlib import Path
from pdf_util.pdf_util import pdf_util

import datetime as dt
import logging
import sys

# Setup Logging
logging.basicConfig(
    # level=logging.ERROR,
    # level=logging.INFO,
    level=logging.DEBUG,
    format=str(dt.datetime.now()).replace(" ", "_") + " | %(asctime)s [%(levelname)s] %(message)s",
    handlers=[
        logging.FileHandler("/var/log/" + str(dt.datetime.today().strftime('%Y-%m-%d')) + "_-_cron.log"),
        logging.StreamHandler(sys.stdout)
    ]
)


app = Flask(__name__)

app.config['UPLOAD_FOLDER'] = 'uploads'


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
        in_filename = pdf_file.filename.rsplit('.', 1)[0]
        filename = os.path.join(app.config['UPLOAD_FOLDER'], pdf_file.filename)
        pdf_file.save(filename)

        # Use pdf_utils Module to split File
        out_filenames = pdf_util(filename).split_pdf()
        logging.debug(out_filenames)

        logging.debug(in_filename)
        logging.debug(os.path.splitext(pdf_file.filename)[0])
        
        shutil.make_archive(in_filename + '_splitted', 'zip', os.path.dirname(filename) + "/split_pdf")
        zip_filename = in_filename + "_splitted.zip"
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
        filename_1 = os.path.join(os.path.dirname(os.path.realpath(__file__)), app.config['UPLOAD_FOLDER'], pdf_file_1.filename)
        pdf_file_1.save(filename_1)

    if pdf_file_2:
        filename_2 = os.path.join(os.path.dirname(os.path.realpath(__file__)), app.config['UPLOAD_FOLDER'], pdf_file_2.filename)
        pdf_file_2.save(filename_2)

    if pdf_file_1 and pdf_file_2:
        logging.debug(filename_1)
        logging.debug(filename_2)

        # Use pdf_utils Module to split File
        out_path = pdf_util(filename_1).merge_pdf_with(filename_2)
        logging.debug(out_path)
        os.rename(out_path, "/app/merge/merger.pdf")

        response = jsonify({"url": '/merge/merger.pdf', "name": os.path.splitext(os.path.basename(out_path))[0]})
        return response


if __name__ == '__main__':

    app.run(debug=True)
