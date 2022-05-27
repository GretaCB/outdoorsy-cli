import pytest
import sys
import os

# Generic way to get the parent directory name
# in case the dirname changes in the future
current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)
# add parent dir to the path so the module is findable
sys.path.append(parent)


from list_customers import Customer, parse_file


@pytest.fixture
def comma_filename():
    return "tests/commas.txt"


@pytest.fixture
def pipe_filename():
    return "tests/pipes.txt"


def test_parse_file_comma(comma_filename):
    expected = [
        Customer('Greta Thunberg', 'greta@future.com', 'sailboat', 'Fridays For Future', '32’'),
        Customer('Xiuhtezcatl Martinez', 'martinez@earthguardian.org', 'campervan', 'Earth Guardian', '28 feet'), 
        Customer('Mandip Singh Soin', 'mandip@ecotourism.net', 'motorboat', 'Frozen Trekker', '32’'), 
        Customer('Jimmy Buffet', 'jb@sailor.com', 'sailboat', 'Margaritaville', '40 ft')
    ]

    assert str(parse_file(comma_filename)) == str(expected)


def test_parse_file_pipe(pipe_filename):
    expected = [
        Customer('Ansel Adams', 'a@adams.com', 'motorboat', 'Rushing Water', '24’'),
        Customer('Steve Irwin', 'steve@crocodiles.com', 'RV', 'G’Day For Adventure', '32 ft'),
        Customer('Isatou Ceesay', 'isatou@recycle.com', 'campervan', 'Plastic To Purses', '20’'),
        Customer('Naomi Uemura', 'n.uemura@gmail.com', 'bicycle', 'Glacier Glider', '5 feet')
    ]

    assert str(parse_file(pipe_filename)) == str(expected)


def test_parse_file_pipe():
    assert parse_file('') == 'File does not exist'
    assert parse_file(None) == 'Filepath must be a string'


def test_sorted_name_parse(pipe_filename):
    expected = [
        Customer('Ansel Adams', 'a@adams.com', 'motorboat', 'Rushing Water', '24’'),
        Customer('Isatou Ceesay', 'isatou@recycle.com', 'campervan', 'Plastic To Purses', '20’'),
        Customer('Naomi Uemura', 'n.uemura@gmail.com', 'bicycle', 'Glacier Glider', '5 feet'),
        Customer('Steve Irwin', 'steve@crocodiles.com', 'RV', 'G’Day For Adventure', '32 ft'),
    ]

    assert str(parse_file(pipe_filename, 'name')) == str(expected)


def test_sorted_vehicle_type_parse(pipe_filename):
    expected = [
        Customer('Steve Irwin', 'steve@crocodiles.com', 'RV', 'G’Day For Adventure', '32 ft'),
        Customer('Naomi Uemura', 'n.uemura@gmail.com', 'bicycle', 'Glacier Glider', '5 feet'),
        Customer('Isatou Ceesay', 'isatou@recycle.com', 'campervan', 'Plastic To Purses', '20’'),
        Customer('Ansel Adams', 'a@adams.com', 'motorboat', 'Rushing Water', '24’'),
    ]

    assert str(parse_file(pipe_filename, 'vehicle_type')) == str(expected)


def test_sorted_name_parse(comma_filename):
    expected = [
        Customer('Greta Thunberg', 'greta@future.com', 'sailboat', 'Fridays For Future', '32’'),
        Customer('Jimmy Buffet', 'jb@sailor.com', 'sailboat', 'Margaritaville', '40 ft'),
        Customer('Mandip Singh Soin', 'mandip@ecotourism.net', 'motorboat', 'Frozen Trekker', '32’'), 
        Customer('Xiuhtezcatl Martinez', 'martinez@earthguardian.org', 'campervan', 'Earth Guardian', '28 feet')
    ]

    assert str(parse_file(comma_filename, 'name')) == str(expected)


def test_sorted_vehicle_type_parse(comma_filename):
    expected = [
        Customer('Xiuhtezcatl Martinez', 'martinez@earthguardian.org', 'campervan', 'Earth Guardian', '28 feet'), 
        Customer('Mandip Singh Soin', 'mandip@ecotourism.net', 'motorboat', 'Frozen Trekker', '32’'), 
        Customer('Greta Thunberg', 'greta@future.com', 'sailboat', 'Fridays For Future', '32’'),
        Customer('Jimmy Buffet', 'jb@sailor.com', 'sailboat', 'Margaritaville', '40 ft')
    ]

    assert str(parse_file(comma_filename, 'vehicle_type')) == str(expected)


def test_unknown_sorted_value(comma_filename):
    expected = [
        Customer('Greta Thunberg', 'greta@future.com', 'sailboat', 'Fridays For Future', '32’'),
        Customer('Xiuhtezcatl Martinez', 'martinez@earthguardian.org', 'campervan', 'Earth Guardian', '28 feet'), 
        Customer('Mandip Singh Soin', 'mandip@ecotourism.net', 'motorboat', 'Frozen Trekker', '32’'), 
        Customer('Jimmy Buffet', 'jb@sailor.com', 'sailboat', 'Margaritaville', '40 ft')
    ]

    # Will return the unsorted list
    assert str(parse_file(comma_filename, 'email')) == str(expected)
