import pytest
from morse import decode


@pytest.mark.parametrize(
    "msg, ret",
    [
        ("... --- ...", "SOS"),
        (".- -... --- -... .-", "ABOBA"),
        (".- .- .-", "AAA")
    ],
)
def test_decode_valid_messages(msg, ret):
    assert decode(msg) == ret
