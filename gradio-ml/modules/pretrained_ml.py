from transformers import pipeline
import numpy as np
from PIL import Image


class PretrainedClassifier:

    PRESETS = {
        "sentiment": {
            "task": "text-classification",
            "model": "distilbert/distilbert-base-uncased-finetuned-sst-2-english"
        },

        "social_sentiment": {
            "task": "text-classification",
            "model": "cardiffnlp/twitter-roberta-base-sentiment-latest"
        },

        "objects": {
            "task": "image-classification",
            "model": "google/vit-base-patch16-224"
        },

        "voice_commands": {
            "task": "audio-classification",
            "model": "superb/wav2vec2-base-superb-ks"
        },

        "general_sounds": {
            "task": "audio-classification",
            "model": "MIT/ast-finetuned-audioset-10-10-0.4593"
        }
    }


    def __init__(
        self,
        preset=None,
        task=None,
        model=None
    ):

        # Use one of our tested presets
        if preset is not None:

            if preset not in self.PRESETS:
                raise ValueError(
                    f"Unknown preset: {preset}\n"
                    f"Available presets: "
                    f"{list(self.PRESETS.keys())}"
                )

            settings = self.PRESETS[preset]

            task = settings["task"]
            model = settings["model"]


        # Or allow students to choose their own model
        if task is None or model is None:
            raise ValueError(
                "Choose a preset OR provide "
                "both task= and model=."
            )


        self.task = task
        self.model_name = model

        print(f"Loading model: {model}")

        self.classifier = pipeline(
            task,
            model=model
        )


    def predict(self, data, top_k=5):

        data = self._prepare_input(data)

        results = self.classifier(
            data,
            top_k=top_k
        )

        # Some pipelines can return nested lists
        if (
            len(results) > 0
            and isinstance(results[0], list)
        ):
            results = results[0]

        top = results[0]

        scores = {
            result["label"]: float(result["score"])
            for result in results
        }

        return {
            "label": top["label"],
            "confidence": float(top["score"]),
            "scores": scores
        }


    def _prepare_input(self, data):

        # ----------------------------
        # AUDIO FROM GRADIO
        # ----------------------------

        if (
            self.task == "audio-classification"
            and isinstance(data, tuple)
        ):

            sample_rate, audio = data

            # Stereo -> mono
            if audio.ndim > 1:
                audio = audio.mean(axis=1)

            # Convert integer audio to float
            if np.issubdtype(audio.dtype, np.integer):
                max_value = np.iinfo(audio.dtype).max

                audio = (
                    audio.astype("float32")
                    / max_value
                )

            else:
                audio = audio.astype("float32")

            return {
                "sampling_rate": sample_rate,
                "raw": audio
            }


        # ----------------------------
        # IMAGE FROM GRADIO
        # ----------------------------

        if (
            self.task == "image-classification"
            and isinstance(data, np.ndarray)
        ):
            return Image.fromarray(
                data.astype("uint8")
            )


        return data


    @classmethod
    def presets(cls):

        return list(cls.PRESETS.keys())