import pytest
import sys
import os

# Generic way to get the parent directory name
# in case the dirname changes in the future
current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)
# add parent dir to the path so the module is findable
sys.path.append(parent)


from list_customers import Customer, read_customers_from_file


@pytest.fixture
def comma_filename():
    return "tests/commas.txt"

@pytest.fixture
def pipe_filename():
    return "tests/pipes.txt"

def test_read_customers_from_file(comma_filename):
    expected = [
        Customer('Xiuhtezcatl Martinez', 'martinez@earthguardian.org', 'campervan', 'Earth Guardian', '28 feet'), 
        Customer('Mandip Singh Soin', 'mandip@ecotourism.net', 'motorboat', 'Frozen Trekker', '32’'), 
        Customer('Jimmy Buffet', 'jb@sailor.com', 'sailboat', 'Margaritaville', '40 ft')
    ]

    assert str(read_customers_from_file(comma_filename)) == str(expected)
