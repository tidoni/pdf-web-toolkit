import os
import shutil
from pdf_util.pdf_project_manager import pdf_project_manager


def test_basic_object_creation():
    test_pdf_project_manager = pdf_project_manager()
    print(test_pdf_project_manager.uuid)
    assert len(test_pdf_project_manager.uuid) == 36

    shutil.rmtree('/app/projects/' + test_pdf_project_manager.uuid)


def test_folder_creation():
    test_pdf_project_manager = pdf_project_manager()
    print(test_pdf_project_manager.uuid)
    assert os.path.isdir('/app/projects/' + test_pdf_project_manager.uuid)

    shutil.rmtree('/app/projects/' + test_pdf_project_manager.uuid)


def test_merge_all_single_pages():
    test_pdf_project_manager = pdf_project_manager()
    print(test_pdf_project_manager.uuid)
    assert os.path.isdir('/app/projects/' + test_pdf_project_manager.uuid)

    test_pdf_project_manager.add_pdf("/app/tests/sample_pdfs/sample_10_page.pdf")
    print(os.path.isfile('/app/projects/' + test_pdf_project_manager.uuid + '/complete.pdf'))
    assert os.path.isfile('/app/projects/' + test_pdf_project_manager.uuid + '/complete.pdf')

    print(os.stat('/app/projects/' + test_pdf_project_manager.uuid + '/complete.pdf').st_size)
    assert os.stat('/app/projects/' + test_pdf_project_manager.uuid + '/complete.pdf').st_size == os.stat("/app/tests/sample_pdfs/sample_10_page.pdf").st_size

    os.remove('/app/projects/' + test_pdf_project_manager.uuid + '/complete.pdf')
    assert not os.path.isfile('/app/projects/' + test_pdf_project_manager.uuid + '/complete.pdf')

    test_pdf_project_manager.merge_all_single_pages()
    print(os.path.isfile('/app/projects/' + test_pdf_project_manager.uuid + '/complete.pdf'))
    assert os.path.isfile('/app/projects/' + test_pdf_project_manager.uuid + '/complete.pdf')

    print(os.stat('/app/projects/' + test_pdf_project_manager.uuid + '/complete.pdf').st_size)
    assert os.stat('/app/projects/' + test_pdf_project_manager.uuid + '/complete.pdf').st_size == 81291

    shutil.rmtree('/app/projects/' + test_pdf_project_manager.uuid)


def test_add_multiple_pdfs():
    test_pdf_project_manager = pdf_project_manager()
    print(test_pdf_project_manager.uuid)
    assert os.path.isdir('/app/projects/' + test_pdf_project_manager.uuid)

    test_pdf_project_manager.add_pdf("/app/tests/sample_pdfs/sample_10_page.pdf")
    print(os.path.isfile('/app/projects/' + test_pdf_project_manager.uuid + '/complete.pdf'))
    assert os.path.isfile('/app/projects/' + test_pdf_project_manager.uuid + '/complete.pdf')

    print(os.path.isdir('/app/projects/' + test_pdf_project_manager.uuid + '/splitted'))
    assert os.path.isdir('/app/projects/' + test_pdf_project_manager.uuid + '/splitted')

    print(os.path.isfile('/app/projects/' + test_pdf_project_manager.uuid + '/splitted/0001.pdf'))
    assert os.path.isfile('/app/projects/' + test_pdf_project_manager.uuid + '/splitted/0001.pdf')

    print(os.stat('/app/projects/' + test_pdf_project_manager.uuid + '/splitted/0001.pdf').st_size)
    assert os.stat('/app/projects/' + test_pdf_project_manager.uuid + '/splitted/0001.pdf').st_size == 3167

    test_pdf_project_manager.add_pdf("/app/tests/sample_pdfs/sample_2_page.pdf")
    print(os.path.isfile('/app/projects/' + test_pdf_project_manager.uuid + '/complete.pdf'))
    assert os.path.isfile('/app/projects/' + test_pdf_project_manager.uuid + '/complete.pdf')

    print(os.stat('/app/projects/' + test_pdf_project_manager.uuid + '/splitted/0001.pdf').st_size)
    assert os.stat('/app/projects/' + test_pdf_project_manager.uuid + '/splitted/0001.pdf').st_size == 3167

    print(os.stat('/app/projects/' + test_pdf_project_manager.uuid + '/splitted/0011.pdf').st_size)
    assert os.stat('/app/projects/' + test_pdf_project_manager.uuid + '/splitted/0011.pdf').st_size == 1804

    print(os.stat('/app/projects/' + test_pdf_project_manager.uuid + '/complete.pdf').st_size)
    assert os.stat('/app/projects/' + test_pdf_project_manager.uuid + '/complete.pdf').st_size == 48408

    shutil.rmtree('/app/projects/' + test_pdf_project_manager.uuid)


def test_move_pages():
    test_pdf_project_manager = pdf_project_manager()
    print(test_pdf_project_manager.uuid)
    assert os.path.isdir('/app/projects/' + test_pdf_project_manager.uuid)

    test_pdf_project_manager.add_pdf("/app/tests/sample_pdfs/sample_10_page.pdf")
    test_pdf_project_manager.add_pdf("/app/tests/sample_pdfs/sample_2_page.pdf")
    print(os.stat('/app/projects/' + test_pdf_project_manager.uuid + '/complete.pdf').st_size)
    assert os.stat('/app/projects/' + test_pdf_project_manager.uuid + '/complete.pdf').st_size == 48408

    os.remove('/app/projects/' + test_pdf_project_manager.uuid + '/complete.pdf')
    assert not os.path.isfile('/app/projects/' + test_pdf_project_manager.uuid + '/complete.pdf')
    test_pdf_project_manager.move_page(1, 4)
    print(os.stat('/app/projects/' + test_pdf_project_manager.uuid + '/splitted/0004.pdf').st_size)
    assert os.stat('/app/projects/' + test_pdf_project_manager.uuid + '/splitted/0004.pdf').st_size == 3167
    print(os.stat('/app/projects/' + test_pdf_project_manager.uuid + '/complete.pdf').st_size)
    assert os.stat('/app/projects/' + test_pdf_project_manager.uuid + '/complete.pdf').st_size == 83909

    os.remove('/app/projects/' + test_pdf_project_manager.uuid + '/complete.pdf')
    assert not os.path.isfile('/app/projects/' + test_pdf_project_manager.uuid + '/complete.pdf')
    test_pdf_project_manager.move_page(4, 1)
    print(os.stat('/app/projects/' + test_pdf_project_manager.uuid + '/splitted/0001.pdf').st_size)
    assert os.stat('/app/projects/' + test_pdf_project_manager.uuid + '/splitted/0001.pdf').st_size == 3167
    print(os.stat('/app/projects/' + test_pdf_project_manager.uuid + '/complete.pdf').st_size)
    assert os.stat('/app/projects/' + test_pdf_project_manager.uuid + '/complete.pdf').st_size == 83908

    os.remove('/app/projects/' + test_pdf_project_manager.uuid + '/complete.pdf')
    assert not os.path.isfile('/app/projects/' + test_pdf_project_manager.uuid + '/complete.pdf')

    test_pdf_project_manager.move_page(1, 12)
    test_pdf_project_manager.move_page(12, 2)
    assert os.stat('/app/projects/' + test_pdf_project_manager.uuid + '/splitted/0002.pdf').st_size == 3167
    print(os.stat('/app/projects/' + test_pdf_project_manager.uuid + '/complete.pdf').st_size)
    assert os.stat('/app/projects/' + test_pdf_project_manager.uuid + '/complete.pdf').st_size == 83909

    shutil.rmtree('/app/projects/' + test_pdf_project_manager.uuid)
