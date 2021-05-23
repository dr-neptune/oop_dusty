import pytest
from src.notebook import Note

# global vars
N1 = Note("Hello First")
N2 = Note("Hello Again")

def test_id_is_incrementing():
    assert N1.id == 1 and N2.id == 2

def test_match_finding_words():
    assert N1.match("First") and not N2.match("Second")
