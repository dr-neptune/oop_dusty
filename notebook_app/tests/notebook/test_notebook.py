import pytest
from src.notebook import Notebook

@pytest.fixture
def n() -> Notebook:
    n = Notebook()
    n.new_note("Hello World", "first")
    n.new_note("Hello Again", "second")
    return n

def test_memo_correctly_added(n) -> None:
    assert n.notes[0].memo == "Hello World" and n.notes[1].memo == "Hello Again"

def test_notebook_search(n) -> None:
    assert len(n.search("Hello")) == 2
    assert len(n.search("World")) == 1

def test_modification_of_memo(n) -> None:
    assert len(n.search("Hello")) == 2
    n.modify_memo(n.notes[0].id, "Hi World")
    assert len(n.search("Hello")) == 1

def test_modification_of_tags(n) -> None:
    assert len(n.search("first")) == 1
    n.modify_tags(n.notes[0].id, "second")
    assert len(n.search("second")) == 2
