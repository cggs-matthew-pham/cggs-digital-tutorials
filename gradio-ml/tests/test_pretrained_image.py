# tests/test_pretrained_image.py

from PIL import Image

from modules import PretrainedClassifier


def test_pretrained_image():
    model = PretrainedClassifier(
        preset="objects"
    )

    image = Image.open(
        "test_fruit.jpg"
    )

    result = model.predict(image)

    assert "label" in result
    assert "confidence" in result
    assert "scores" in result

    assert isinstance(
        result["label"],
        str
    )

    assert 0 <= result["confidence"] <= 1