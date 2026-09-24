from pathlib import Path

from modules import ImageClassifier


def test_image_classifier():
    dataset = Path("tests/files/fruit")
    test_image = Path("tests/files/test_fruit.jpg")

    model = ImageClassifier(dataset)

    model.train(epochs=1)

    result = model.predict(test_image)

    assert isinstance(result, dict)
    assert "apple" in result
    assert "banana" in result