import what_is_year_now
from unittest.mock import patch
from json import dumps
import pytest


def test_ymd():
    with patch("what_is_year_now.urllib.request.urlopen") as mock_urlopen:
        mock_urlopen.return_value.__enter__.return_value.read.return_value = \
            dumps({'currentDateTime': '2025-11-13T10:55Z'})
        result = what_is_year_now.what_is_year_now()
    assert result == 2025


def test_dmy():
    with patch("what_is_year_now.urllib.request.urlopen") as mock_urlopen:
        mock_urlopen.return_value.__enter__.return_value.read.return_value = \
            dumps({'currentDateTime': '22.01.2025'})
        result = what_is_year_now.what_is_year_now()
    assert result == 2025


def test_invalid_format():
    with patch("what_is_year_now.urllib.request.urlopen") as mock_urlopen:
        mock_urlopen.return_value.__enter__.return_value.read.return_value = \
            dumps({'currentDateTime': '1.1.2008'})
        with pytest.raises(ValueError, match='Invalid format'):
            what_is_year_now.what_is_year_now()
