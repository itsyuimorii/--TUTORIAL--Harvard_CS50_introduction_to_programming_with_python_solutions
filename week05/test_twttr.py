from twttr import shorten

def test_twttr():
    assert shorten("CS50") == "CS50"
    assert shorten("this is python cs50") == "ths s pythn cs50"
    assert shorten("yui morii") == "y mr"
    assert shorten("PYTHON") == "PYTHN"
    assert shorten("Canada.") == "Cnd."

