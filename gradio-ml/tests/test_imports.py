from modules import (
    ImageClassifier,
    PretrainedClassifier,
    TextReader,
)


def test_imports():
    assert ImageClassifier is not None
    assert PretrainedClassifier is not None
    assert TextReader is not None
