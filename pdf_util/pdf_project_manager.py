import uuid
import os
import shutil
import traceback
import glob

import datetime as dt
import logging
import sys

from pdf_util.pdf_util import pdf_util

base_path = "/app/projects/"

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


class pdf_project_manager:
    def __init__(self, uuid4=None):
        if uuid4 is not None:
            self.uuid = uuid4
        else:
            self.uuid = str(uuid.uuid4())

        try:
            self.pdf_init = os.path.isfile('/app/projects/' + self.uuid + '/complete.pdf')
        except Exception as e:
            logging.warning("Error looking up file: " + str(e))
            logging.warning("Stacktrace: " + str(traceback.format_exc()))
            self.pdf_init = False

        os.makedirs(base_path + self.uuid, exist_ok=True)
        self.pdf_handler = None

    def merge_all_single_pages(self):
        listing = glob.glob(base_path + self.uuid + '/splitted/*.pdf')
        listing.sort()
        shutil.copyfile(listing.pop(0), base_path + self.uuid + "/complete.pdf")

        for pdf_file in listing:
            print(pdf_file)
            pdf_util(base_path + self.uuid + "/complete.pdf").merge_pdf_with_and_location(pdf_file, base_path + self.uuid + "/tmp_complete.pdf")
            shutil.copyfile(base_path + self.uuid + "/tmp_complete.pdf", base_path + self.uuid + "/complete.pdf")
            os.remove(base_path + self.uuid + "/tmp_complete.pdf")

    def add_pdf(self, pdf_path):
        if not self.pdf_init:
            shutil.copyfile(pdf_path, base_path + self.uuid + "/complete.pdf")
            self.pdf_handler = pdf_util(base_path + self.uuid + "/complete.pdf")
            self.pdf_init = True
        else:
            shutil.copyfile(pdf_path, base_path + self.uuid + "/tmp.pdf")
            pdf_util(base_path + self.uuid + "/complete.pdf").merge_pdf_with_and_location(base_path + self.uuid + "/tmp.pdf", base_path + self.uuid + "/tmp_complete.pdf")
            shutil.copyfile(base_path + self.uuid + "/tmp_complete.pdf", base_path + self.uuid + "/complete.pdf")
            os.remove(base_path + self.uuid + "/tmp_complete.pdf")
            os.remove(base_path + self.uuid + "/tmp.pdf")
            self.pdf_handler = pdf_util(base_path + self.uuid + "/complete.pdf")

        self.pdf_handler.split_pdf_with_location(base_path + self.uuid + '/splitted/', True, True)

    def move_page(self, from_location, to_location):
        try:
            if from_location <= 0 or to_location <= 0:
                raise ValueError("Pagenumber smaller/equal Zero")

            if from_location < to_location:
                shutil.move(base_path + self.uuid + '/splitted/' + str(from_location).zfill(4) + '.pdf', base_path + self.uuid + '/splitted/tmp.pdf')
                for num in range(from_location, to_location):
                    print(num)
                    shutil.move(base_path + self.uuid + '/splitted/' + str(num + 1).zfill(4) + '.pdf', base_path + self.uuid + '/splitted/' + str(num).zfill(4) + '.pdf')
                shutil.move(base_path + self.uuid + '/splitted/tmp.pdf', base_path + self.uuid + '/splitted/' + str(to_location).zfill(4) + '.pdf')

            elif from_location > to_location:
                shutil.move(base_path + self.uuid + '/splitted/' + str(from_location).zfill(4) + '.pdf', base_path + self.uuid + '/splitted/tmp.pdf')
                for num in reversed(range(to_location, from_location)):
                    print(num)
                    print("move: " + str(num).zfill(4) + " | to: " + str(num + 1).zfill(4))
                    shutil.move(base_path + self.uuid + '/splitted/' + str(num).zfill(4) + '.pdf', base_path + self.uuid + '/splitted/' + str(num + 1).zfill(4) + '.pdf')
                shutil.move(base_path + self.uuid + '/splitted/tmp.pdf', base_path + self.uuid + '/splitted/' + str(to_location).zfill(4) + '.pdf')
            else:
                raise ValueError("from_location and to_location are the same")

            self.merge_all_single_pages()

        except Exception as e:
            logging.error("Error while moving page: " + str(e))
            logging.error("Stacktrace: " + str(traceback.format_exc()))
