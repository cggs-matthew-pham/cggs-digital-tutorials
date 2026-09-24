from pathlib import Path

import pytest
import pytesseract
from PIL import Image

from modules import TextReader


def test_text_reader():
    image_file = Path("tests/files/hello.png")

    try:
        pytesseract.get_tesseract_version()
    except Exception:
        pytest.skip(
            "Tesseract OCR is not installed or not on PATH."
        )

    reader = TextReader()
    image = Image.open(image_file)

    result = reader.read(image)

    assert isinstance(result, str)
    assert len(result) > 0
