import os
import pytesseract


pytesseract.pytesseract.tesseract_cmd = os.path.expandvars(
    r"%LOCALAPPDATA%\Programs\Tesseract-OCR\tesseract.exe"
)


class TextReader:
    def read(self, image):
        text = pytesseract.image_to_string(image)

        if text.strip() == "":
            return "No text found."

        return text.strip()