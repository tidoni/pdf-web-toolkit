import pytest
import os
from pdf_util.pdf_util import pdf_util

def test_split_pages():
    # Single Pages
    test_file = pdf_util("/app/tests/sample_pdfs/sample_1_page.pdf").split_pdf()
    print(test_file)

    print(os.stat("/app/tests/sample_pdfs/split_pdf/sample_1_page_1.pdf").st_size)
    assert os.stat("/app/tests/sample_pdfs/split_pdf/sample_1_page_1.pdf").st_size == 69339
    
    # Two Pages
    test_file = pdf_util("/app/tests/sample_pdfs/sample_2_page.pdf").split_pdf()
    print(test_file)

    print(os.stat("/app/tests/sample_pdfs/split_pdf/sample_2_page_1.pdf").st_size)
    assert os.stat("/app/tests/sample_pdfs/split_pdf/sample_2_page_1.pdf").st_size == 1804
    print(os.stat("/app/tests/sample_pdfs/split_pdf/sample_2_page_2.pdf").st_size)
    assert os.stat("/app/tests/sample_pdfs/split_pdf/sample_2_page_2.pdf").st_size == 1405
    
    # Ten Pages
    test_file = pdf_util("/app/tests/sample_pdfs/sample_10_page.pdf").split_pdf()
    print(test_file)

    print(os.stat("/app/tests/sample_pdfs/split_pdf/sample_10_page_1.pdf").st_size)
    assert os.stat("/app/tests/sample_pdfs/split_pdf/sample_10_page_1.pdf").st_size == 3167
    print(os.stat("/app/tests/sample_pdfs/split_pdf/sample_10_page_2.pdf").st_size)
    assert os.stat("/app/tests/sample_pdfs/split_pdf/sample_10_page_2.pdf").st_size == 2888
    print(os.stat("/app/tests/sample_pdfs/split_pdf/sample_10_page_3.pdf").st_size)
    assert os.stat("/app/tests/sample_pdfs/split_pdf/sample_10_page_3.pdf").st_size == 6670
    print(os.stat("/app/tests/sample_pdfs/split_pdf/sample_10_page_4.pdf").st_size)
    assert os.stat("/app/tests/sample_pdfs/split_pdf/sample_10_page_4.pdf").st_size == 3043
    print(os.stat("/app/tests/sample_pdfs/split_pdf/sample_10_page_5.pdf").st_size)
    assert os.stat("/app/tests/sample_pdfs/split_pdf/sample_10_page_5.pdf").st_size == 9968
    print(os.stat("/app/tests/sample_pdfs/split_pdf/sample_10_page_6.pdf").st_size)
    assert os.stat("/app/tests/sample_pdfs/split_pdf/sample_10_page_6.pdf").st_size == 5367
    print(os.stat("/app/tests/sample_pdfs/split_pdf/sample_10_page_7.pdf").st_size)
    assert os.stat("/app/tests/sample_pdfs/split_pdf/sample_10_page_7.pdf").st_size == 10093
    print(os.stat("/app/tests/sample_pdfs/split_pdf/sample_10_page_8.pdf").st_size)
    assert os.stat("/app/tests/sample_pdfs/split_pdf/sample_10_page_8.pdf").st_size == 8578
    print(os.stat("/app/tests/sample_pdfs/split_pdf/sample_10_page_9.pdf").st_size)
    assert os.stat("/app/tests/sample_pdfs/split_pdf/sample_10_page_9.pdf").st_size == 30188
    print(os.stat("/app/tests/sample_pdfs/split_pdf/sample_10_page_10.pdf").st_size)
    assert os.stat("/app/tests/sample_pdfs/split_pdf/sample_10_page_10.pdf").st_size == 3789
    

def test_merge_with():
    # Write test code to verify the behavior of the merge_with method
    pass

def test_rotate_pages():
    # Write test code to verify the behavior of the rotate_pages method
    pass

def test_ocr_pages():
    # Write test code to verify the behavior of the rotate_pages method
    pass
