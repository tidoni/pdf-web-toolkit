import shutil
import os
import glob
import traceback
from flask import Flask, render_template, request, redirect, jsonify, send_from_directory
from pdf_util.pdf_project_manager import pdf_project_manager

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


@app.route('/app/')
def pdf_app():
    return render_template('app.html')


@app.route('/split/<path:path>')
def send_report(path):
    return send_from_directory('split', path)


@app.route('/merge/<path:path>')
def send_merge(path):
    return send_from_directory('merge', path)


@app.route('/projects/<path:path>')
def get_project(path):
    return send_from_directory('projects', path)


@app.route('/get_single_pages_archive/<uuid>/')
def get_single_pages_archive(uuid):
    try:
        shutil.make_archive('pdf_splitted', 'zip', "/app/projects/" + uuid + '/splitted')
        os.rename('/app/pdf_splitted.zip', '/app/projects/' + uuid + '/pdf_splitted.zip')
        response = jsonify({'status': 200, 'url': '/projects/' + uuid + '/pdf_splitted.zip'})
    except Exception as e:
        logging.debug("There was an error: " + str(e))
        logging.debug("Stacktrace: " + str(traceback.format_exc()))
        response = jsonify({"status": 500, "error_message": e})
    return response


@app.route('/get_single_pages_info/<uuid>/')
def get_single_pages_info(uuid):
    try:
        pages = []

        page_list = glob.glob("/app/projects/" + uuid + "/splitted/*.pdf")
        logging.debug("page_list: ")
        logging.debug(page_list)

        page_list.sort()
        logging.debug("sorted_page_list: ")
        logging.debug(page_list)

        for file in page_list:
            pages.append(file[4:])  # Cut of /app
        response = jsonify({'status': 200, 'pages': pages})
    except Exception as e:
        logging.debug("There was an error: " + str(e))
        logging.debug("Stacktrace: " + str(traceback.format_exc()))
        response = jsonify({"status": 500, "error_message": e})
    return response


@app.route('/split_to_zip', methods=['POST'])
def split_to_zip():
    if 'pdf_1' not in request.files:
        return redirect(request.url)

    pdf_file = request.files['pdf_1']

    if pdf_file.filename == '':
        return redirect(request.url)

    if pdf_file:
        in_filename = pdf_file.filename.rsplit('.', 1)[0]
        filename = os.path.join(app.config['UPLOAD_FOLDER'], pdf_file.filename)
        pdf_file.save(filename)

        # Use pdf_project_manager to split File
        pdf_project = pdf_project_manager()
        pdf_project.add_pdf(filename)

        logging.debug(in_filename)
        logging.debug(os.path.splitext(pdf_file.filename)[0])

        shutil.make_archive(in_filename + '_splitted', 'zip', "/app/projects/" + pdf_project.uuid + '/splitted')
        zip_filename = in_filename + "_splitted.zip"
        os.rename("/app/" + zip_filename, "/app/split/" + zip_filename)

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

        # Use pdf_project_manager to split File
        pdf_project = pdf_project_manager()
        pdf_project.add_pdf(filename_1)
        pdf_project.add_pdf(filename_2)
        out_path = "/app/projects/" + pdf_project.uuid + "/complete.pdf"
        logging.debug(out_path)
        os.rename(out_path, "/app/merge/merger.pdf")

        response = jsonify({"url": '/merge/merger.pdf', "name": os.path.splitext(os.path.basename(out_path))[0]})
        return response


@app.route('/init_project/', methods=['GET'])
def init_project():
    try:
        pdf_project = pdf_project_manager()
        response = jsonify({"status": 200, "project_uuid": pdf_project.uuid})
    except Exception as e:
        logging.debug("There was an error: " + str(e))
        logging.debug("Stacktrace: " + str(traceback.format_exc()))
        response = jsonify({"status": 500, "project_uuid": ''})
    return response


@app.route('/add_pdf_to_project/', methods=['POST'])
def add_pdf_to_project():
    try:
        if 'pdf' not in request.files:
            logging.debug(request)
            return redirect(request.url)
        else:
            pdf_file = request.files['pdf']
            filename_1 = os.path.join(os.path.dirname(os.path.realpath(__file__)), app.config['UPLOAD_FOLDER'], pdf_file.filename)
            pdf_file.save(filename_1)

        pdf_file = request.files['pdf']
        uuid = request.form['uuid']
        logging.debug(pdf_file)
        logging.debug(uuid)

        pdf_project = pdf_project_manager(uuid4=uuid)
        pdf_project.add_pdf(filename_1)

        response = jsonify({"status": 200, "message": 'PDF added'})
    except Exception as e:
        logging.debug("There was an error: " + str(e))
        logging.debug("Stacktrace: " + str(traceback.format_exc()))
        response = jsonify({"status": 500, "error_message": e})

    return response


if __name__ == '__main__':

    app.run(debug=True)
