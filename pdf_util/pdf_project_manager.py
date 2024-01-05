from pypdf import PdfReader, PdfWriter
import uuid
import os
import shutil

import datetime as dt
import logging
import sys


from pdf_util.pdf_util import pdf_util


# Setup Logging
logging.basicConfig(
    # level=logging.ERROR,
    # level=logging.INFO,
    level=logging.DEBUG,
    format=str(dt.datetime.now()).replace(" ", "_") + " | %(asctime)s [%(levelname)s] %(message)s",
    handlers=[
        logging.FileHandler("/var/log/" + str(dt.datetime.today().strftime('%Y-%m-%d')) + "_-_pdf_project_manager.log"),
        logging.StreamHandler(sys.stdout)
    ]
)

base_path = "/app/projects/"

class pdf_project_manager:
    def __init__(self):
        self.uuid = str(uuid.uuid4())
        self.pdf_init = False
        self.project_name = ""
        os.makedirs(base_path + self.uuid, exist_ok=True)


    """
    def add_pdf(self, pdf_path):
        if self.pdf_init:
            shutil.copyfile(pdf_path, base_path + self.uuid + "/complete.pdf")
        else:
            shutil.copyfile(pdf_path, base_path + self.uuid + "/tmp.pdf")
            pdf_util(base_path + self.uuid + "/complete.pdf").merge_pdf_with_and_location(base_path + self.uuid + "/tmp.pdf", base_path + self.uuid + "/tmp_complete.pdf")
            shutil.copyfile(base_path + self.uuid + "/tmp_complete.pdf", base_path + self.uuid + "/complete.pdf")
            os.remove(base_path + self.uuid + "/tmp_complete.pdf")
            os.remove(base_path + self.uuid + "/tmp.pdf")

        # Splitt files in all single Pages in Subdirectory...
    """