import os
from pypdf import PdfReader, PdfWriter

class pdf_util:
    def __init__(self, file_path):
        self.file_path = file_path
        self.file_name = os.path.basename(file_path)
        self.file_name_wo_extension = os.path.splitext(os.path.basename(file_path))[0]


    def split_pdf(self):
        out_filenames = []
        os.makedirs(os.path.dirname(self.file_path) + "/split_pdf", exist_ok=True)
        with open(self.file_path, 'rb') as pdf_file:
            pdf_reader = PdfReader(pdf_file)
            num_pages = len(pdf_reader.pages)
            for page_num in range(num_pages):

                writer = PdfWriter()
                writer.add_page(pdf_reader.pages[page_num])

                out_filename = os.path.dirname(self.file_path) + '/split_pdf/' + self.file_name_wo_extension + '_' + str(page_num + 1) + '.pdf'
                with open(out_filename, 'wb') as outfile:
                    writer.write(outfile)
                    out_filenames.append(out_filename)

        return out_filenames


    def merge_pdf_with(self, merge_file_path, merged_name="merged"):
        os.makedirs(os.path.dirname(self.file_path) + "/merge_pdf", exist_ok=True)
        pdf_reader_1 = PdfReader(self.file_path)
        pdf_reader_2 = PdfReader(merge_file_path)
        writer = PdfWriter()

        for page_num in range(len(pdf_reader_1.pages)):
            writer.add_page(pdf_reader_1.pages[page_num])

        for page_num in range(len(pdf_reader_2.pages)):
            writer.add_page(pdf_reader_2.pages[page_num])

        out_path = os.path.dirname(self.file_path) + "/merge_pdf" + '/merger.pdf'
        with open(out_path, 'wb') as outfile:
            writer.write(outfile)

        return out_path
