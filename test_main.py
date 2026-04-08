import pytest
from main import count_words, count_sentences


# ======= ФІКСТУРИ =======

@pytest.fixture
def simple_text():
    return "Python is a great language. It is easy to learn!"


@pytest.fixture
def complex_text():
    return "Python is a great language. It is easy to learn! Do you like coding? I love it..."


# ======= ТЕСТИ З ФІКСТУРАМИ =======

def test_count_words_simple(simple_text):
    assert count_words(simple_text) == 8


def test_count_sentences_simple(simple_text):
    assert count_sentences(simple_text) == 2


def test_count_sentences_complex(complex_text):
    assert count_sentences(complex_text) == 4


# ======= ПАРАМЕТРИЗАЦІЯ =======

@pytest.mark.parametrize("text, expected_words", [
    ("Python is great", 3),
    ("I love coding every day", 5),
    ("Hello", 1),
    ("Easy, fast, simple", 3),
])
def test_count_words_parametrized(text, expected_words):
    assert count_words(text) == expected_words


@pytest.mark.parametrize("text, expected_sentences", [
    ("Hello!", 1),
    ("How are you? I am fine.", 2),
    ("Stop... Go! Okay.", 3),
    ("No punctuation here", 0),
])
def test_count_sentences_parametrized(text, expected_sentences):
    assert count_sentences(text) == expected_sentences