import pytest
import os
import shutil
from pdf_util.pdf_util import pdf_util

def test_split_pdf():
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

    shutil.rmtree("/app/tests/sample_pdfs/split_pdf/")


def test_split_pdf_and_location():
    # Single Pages
    test_file = pdf_util("/app/tests/sample_pdfs/sample_1_page.pdf").split_pdf_with_location("/tmp/test_directory/", False)
    print(test_file)
    print(os.stat("/tmp/test_directory/sample_1_page_1.pdf").st_size)
    assert os.stat("/tmp/test_directory/sample_1_page_1.pdf").st_size == 69339
    
    test_file = pdf_util("/app/tests/sample_pdfs/sample_1_page.pdf").split_pdf_with_location("/tmp/test_directory/", True)
    print(test_file)
    print(os.stat("/tmp/test_directory/1.pdf").st_size)
    assert os.stat("/tmp/test_directory/1.pdf").st_size == 69339
    
    shutil.rmtree("/tmp/test_directory/")


    # Two Pages
    test_file = pdf_util("/app/tests/sample_pdfs/sample_2_page.pdf").split_pdf_with_location("/tmp/test_directory/", False)
    print(test_file)
    print(os.stat("/tmp/test_directory/sample_2_page_1.pdf").st_size)
    assert os.stat("/tmp/test_directory/sample_2_page_1.pdf").st_size == 1804
    print(os.stat("/tmp/test_directory/sample_2_page_2.pdf").st_size)
    assert os.stat("/tmp/test_directory/sample_2_page_2.pdf").st_size == 1405

    # Two Pages
    test_file = pdf_util("/app/tests/sample_pdfs/sample_2_page.pdf").split_pdf_with_location("/tmp/test_directory/", True)
    print(test_file)
    print(os.stat("/tmp/test_directory/1.pdf").st_size)
    assert os.stat("/tmp/test_directory/1.pdf").st_size == 1804
    print(os.stat("/tmp/test_directory/2.pdf").st_size)
    assert os.stat("/tmp/test_directory/2.pdf").st_size == 1405
    
    shutil.rmtree("/tmp/test_directory/")


    # Ten Pages
    test_file = pdf_util("/app/tests/sample_pdfs/sample_10_page.pdf").split_pdf_with_location("/tmp/test_directory/", False)
    print(test_file)
    print(os.stat("/tmp/test_directory/sample_10_page_1.pdf").st_size)
    assert os.stat("/tmp/test_directory/sample_10_page_1.pdf").st_size == 3167
    print(os.stat("/tmp/test_directory/sample_10_page_2.pdf").st_size)
    assert os.stat("/tmp/test_directory/sample_10_page_2.pdf").st_size == 2888
    print(os.stat("/tmp/test_directory/sample_10_page_3.pdf").st_size)
    assert os.stat("/tmp/test_directory/sample_10_page_3.pdf").st_size == 6670
    print(os.stat("/tmp/test_directory/sample_10_page_4.pdf").st_size)
    assert os.stat("/tmp/test_directory/sample_10_page_4.pdf").st_size == 3043
    print(os.stat("/tmp/test_directory/sample_10_page_5.pdf").st_size)
    assert os.stat("/tmp/test_directory/sample_10_page_5.pdf").st_size == 9968
    print(os.stat("/tmp/test_directory/sample_10_page_6.pdf").st_size)
    assert os.stat("/tmp/test_directory/sample_10_page_6.pdf").st_size == 5367
    print(os.stat("/tmp/test_directory/sample_10_page_7.pdf").st_size)
    assert os.stat("/tmp/test_directory/sample_10_page_7.pdf").st_size == 10093
    print(os.stat("/tmp/test_directory/sample_10_page_8.pdf").st_size)
    assert os.stat("/tmp/test_directory/sample_10_page_8.pdf").st_size == 8578
    print(os.stat("/tmp/test_directory/sample_10_page_9.pdf").st_size)
    assert os.stat("/tmp/test_directory/sample_10_page_9.pdf").st_size == 30188
    print(os.stat("/tmp/test_directory/sample_10_page_10.pdf").st_size)
    assert os.stat("/tmp/test_directory/sample_10_page_10.pdf").st_size == 3789

    test_file = pdf_util("/app/tests/sample_pdfs/sample_10_page.pdf").split_pdf_with_location("/tmp/test_directory/", True)
    print(test_file)
    print(os.stat("/tmp/test_directory/1.pdf").st_size)
    assert os.stat("/tmp/test_directory/1.pdf").st_size == 3167
    print(os.stat("/tmp/test_directory/2.pdf").st_size)
    assert os.stat("/tmp/test_directory/2.pdf").st_size == 2888
    print(os.stat("/tmp/test_directory/3.pdf").st_size)
    assert os.stat("/tmp/test_directory/3.pdf").st_size == 6670
    print(os.stat("/tmp/test_directory/4.pdf").st_size)
    assert os.stat("/tmp/test_directory/4.pdf").st_size == 3043
    print(os.stat("/tmp/test_directory/5.pdf").st_size)
    assert os.stat("/tmp/test_directory/5.pdf").st_size == 9968
    print(os.stat("/tmp/test_directory/6.pdf").st_size)
    assert os.stat("/tmp/test_directory/6.pdf").st_size == 5367
    print(os.stat("/tmp/test_directory/7.pdf").st_size)
    assert os.stat("/tmp/test_directory/7.pdf").st_size == 10093
    print(os.stat("/tmp/test_directory/8.pdf").st_size)
    assert os.stat("/tmp/test_directory/8.pdf").st_size == 8578
    print(os.stat("/tmp/test_directory/9.pdf").st_size)
    assert os.stat("/tmp/test_directory/9.pdf").st_size == 30188
    print(os.stat("/tmp/test_directory/10.pdf").st_size)
    assert os.stat("/tmp/test_directory/10.pdf").st_size == 3789

    shutil.rmtree("/tmp/test_directory/")


def test_merge_pdf_with():
    test_file = pdf_util("/app/tests/sample_pdfs/sample_1_page.pdf").merge_pdf_with("/app/tests/sample_pdfs/sample_2_page.pdf")
    print(test_file)
    print(os.stat("/app/tests/sample_pdfs/merge_pdf/merger.pdf").st_size)
    assert os.stat("/app/tests/sample_pdfs/merge_pdf/merger.pdf").st_size == 71761

    test_file = pdf_util("/app/tests/sample_pdfs/sample_1_page.pdf").merge_pdf_with("/app/tests/sample_pdfs/sample_10_page.pdf")
    print(test_file)
    print(os.stat("/app/tests/sample_pdfs/merge_pdf/merger.pdf").st_size)
    assert os.stat("/app/tests/sample_pdfs/merge_pdf/merger.pdf").st_size == 115044

    test_file = pdf_util("/app/tests/sample_pdfs/sample_2_page.pdf").merge_pdf_with("/app/tests/sample_pdfs/sample_10_page.pdf")
    print(test_file)
    print(os.stat("/app/tests/sample_pdfs/merge_pdf/merger.pdf").st_size)
    assert os.stat("/app/tests/sample_pdfs/merge_pdf/merger.pdf").st_size == 48427

    shutil.rmtree("/app/tests/sample_pdfs/merge_pdf/")


def test_merge_pdf_with_and_location():
    test_file = pdf_util("/app/tests/sample_pdfs/sample_1_page.pdf").merge_pdf_with_and_location("/app/tests/sample_pdfs/sample_2_page.pdf", "/tmp/test_directory/merged_file.pdf")
    print(test_file)
    print(os.stat("/tmp/test_directory/merged_file.pdf").st_size)
    assert os.stat("/tmp/test_directory/merged_file.pdf").st_size == 71761
    shutil.rmtree("/tmp/test_directory/")

    test_file = pdf_util("/app/tests/sample_pdfs/sample_1_page.pdf").merge_pdf_with_and_location("/app/tests/sample_pdfs/sample_10_page.pdf", "/tmp/test_directory/merge_pdf/merger.pdf")
    print(test_file)
    print(os.stat("/tmp/test_directory/merge_pdf/merger.pdf").st_size)
    assert os.stat("/tmp/test_directory/merge_pdf/merger.pdf").st_size == 115044
    shutil.rmtree("/tmp/test_directory/")

    test_file = pdf_util("/app/tests/sample_pdfs/sample_2_page.pdf").merge_pdf_with_and_location("/app/tests/sample_pdfs/sample_10_page.pdf", "/tmp/test_directory/merge_pdf/bigfile.pdf")
    print(test_file)
    print(os.stat("/tmp/test_directory/merge_pdf/bigfile.pdf").st_size)
    assert os.stat("/tmp/test_directory/merge_pdf/bigfile.pdf").st_size == 48427

    shutil.rmtree("/tmp/test_directory/")

def test_rotate_pages():
    # Write test code to verify the behavior of the rotate_pages method
    pass

def test_ocr_pages():
    # Write test code to verify the behavior of the rotate_pages method
    pass
