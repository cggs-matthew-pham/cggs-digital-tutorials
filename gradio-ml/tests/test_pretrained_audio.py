# tests/test_pretrained_audio.py

import numpy as np

from modules import PretrainedClassifier


def make_test_audio():
    sample_rate = 16000

    audio = np.zeros(
        sample_rate,
        dtype=np.int16
    )

    return sample_rate, audio


def test_voice_commands():
    model = PretrainedClassifier(
        preset="voice_commands"
    )

    result = model.predict(
        make_test_audio()
    )

    assert "label" in result
    assert "confidence" in result
    assert "scores" in result

    assert 0 <= result["confidence"] <= 1


def test_general_sounds():
    model = PretrainedClassifier(
        preset="general_sounds"
    )

    result = model.predict(
        make_test_audio()
    )

    assert "label" in result
    assert "confidence" in result
    assert "scores" in result

    assert 0 <= result["confidence"] <= 1