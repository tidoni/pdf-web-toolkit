import pytest
import os
from pdf_util.pdf_project_manager import pdf_project_manager

def test_basic_object_creation():
    test_pdf_project_manager = pdf_project_manager()
    print(test_pdf_project_manager.uuid)
    assert len(test_pdf_project_manager.uuid) == 36


def test_folder_creation():
    test_pdf_project_manager = pdf_project_manager()
    print(test_pdf_project_manager.uuid)
    assert os.path.isdir('/app/projects/' + test_pdf_project_manager.uuid)

