from names import make_full_name, \
    extract_family_name, extract_given_name
import pytest

def test_make_full_name():
    assert make_full_name("Brown", "Sally") == "Sally; Brown"
    assert make_full_name("McDonald", "Ronald") == "Ronald; McDonald"
    assert make_full_name("Schwarzenegger", "Arnold") == "Arnold; Schwarzenegger"
    assert make_full_name("O-Reilly", "Auto") == "Auto; O-Reilly"

def test_extract_family_name():
    assert extract_family_name("Brown; Sally") == "Brown"
    assert extract_family_name("McDonald; Ronald") == "McDonald"
    assert extract_family_name("Schwarzenegger; Arnold") == "Schwarzenegger"
    assert extract_family_name("O-Reilly; Auto") == "O-Reilly"

def test_extract_given_name():
    assert extract_given_name("Brown; Sally") == "Sally"
    assert extract_given_name("McDonald; Ronald") == "Ronald"
    assert extract_given_name("Schwarzenegger; Arnold") == "Arnold"
    assert extract_given_name("O-Reilly; Auto") == "Auto"
pytest.main(["-v", "--tb=line", "-rN", __file__])