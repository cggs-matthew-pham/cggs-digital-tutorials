# tests/test_presets.py

from modules import PretrainedClassifier


def test_presets_exist():

    presets = PretrainedClassifier.presets()

    assert "sentiment" in presets
    assert "social_sentiment" in presets
    assert "objects" in presets
    assert "voice_commands" in presets
    assert "general_sounds" in presets