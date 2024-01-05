from pypdf import PdfReader, PdfWriter
import uuid
import os

class pdf_project_manager:
    def __init__(self):
        self.uuid = str(uuid.uuid4())
        os.makedirs("/app/projects/" + self.uuid, exist_ok=True)

