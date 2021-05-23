import pytest
from typing import Tuple
from src.notebook import Note

# global vars
@pytest.fixture
def notes() -> Tuple[Note, Note]:
    N1 = Note("Hello First")
    N2 = Note("Hello Again")
    return (N1, N2)

def test_id_is_incrementing(notes) -> None:
    assert notes[0].id == 1 and notes[1].id == 2

def test_match_finding_words(notes) -> None:
    assert notes[0].match("First") and not notes[1].match("Second")
