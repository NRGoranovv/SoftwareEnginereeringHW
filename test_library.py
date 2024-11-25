import pytest
from library import get_status_code

def test_get_status_code_success():
    # Симулира успешна заявка към добре известен URL
    url = "https://httpbin.org/status/200"
    result = get_status_code(url)
    assert result == 200

def test_get_status_code_error():
    # Симулира грешка със счупен URL
    url = "http://invalid.url"
    result = get_status_code(url)
    assert isinstance(result, str) and result.startswith("Error:")
