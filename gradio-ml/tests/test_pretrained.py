from modules import PretrainedClassifier


def test_social_sentiment():
    model = PretrainedClassifier(
        preset="social_sentiment"
    )

    result = model.predict(
        "I really enjoyed this."
    )

    assert "label" in result
    assert "confidence" in result
    assert "scores" in result

    assert 0 <= result["confidence"] <= 1
