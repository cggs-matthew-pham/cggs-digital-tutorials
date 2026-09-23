# pattern_ml.py

import json
import os

import keras
import numpy as np
from keras import layers


class ImageClassifier:

    def __init__(
        self,
        data_folder=None,
        image_size=(160, 160),
        validation_split=0.2
    ):
        self.data_folder = data_folder
        self.image_size = image_size
        self.validation_split = validation_split

        self.model = None
        self.class_names = None
        self.train_data = None
        self.validation_data = None

        if data_folder:
            self._load_data()
            self._build_model()


    def _load_data(self):

        self.train_data = keras.utils.image_dataset_from_directory(
            self.data_folder,
            validation_split=self.validation_split,
            subset="training",
            seed=42,
            image_size=self.image_size,
            batch_size=32
        )

        self.validation_data = keras.utils.image_dataset_from_directory(
            self.data_folder,
            validation_split=self.validation_split,
            subset="validation",
            seed=42,
            image_size=self.image_size,
            batch_size=32
        )

        self.class_names = self.train_data.class_names

        print("Classes found:", self.class_names)


    def _build_model(self):

        base_model = keras.applications.MobileNetV2(
            input_shape=(*self.image_size, 3),
            include_top=False,
            weights="imagenet"
        )

        # Keep the pretrained image knowledge
        base_model.trainable = False

        inputs = keras.Input(shape=(*self.image_size, 3))

        # MobileNetV2 expects values between -1 and 1
        x = layers.Rescaling(
            scale=1 / 127.5,
            offset=-1
        )(inputs)

        x = base_model(x, training=False)

        x = layers.GlobalAveragePooling2D()(x)

        outputs = layers.Dense(
            len(self.class_names),
            activation="softmax"
        )(x)

        self.model = keras.Model(inputs, outputs)

        self.model.compile(
            optimizer="adam",
            loss="sparse_categorical_crossentropy",
            metrics=["accuracy"]
        )


    def train(self, epochs=5):

        print("Training classes:", self.class_names)

        history = self.model.fit(
            self.train_data,
            validation_data=self.validation_data,
            epochs=epochs
        )

        return history


    def accuracy(self):

        loss, accuracy = self.model.evaluate(
            self.validation_data,
            verbose=0
        )

        print(f"Validation accuracy: {accuracy:.1%}")

        return accuracy


    def predict(self, image_file):

        image = keras.utils.load_img(
            image_file,
            target_size=self.image_size
        )

        image = keras.utils.img_to_array(image)

        image = np.expand_dims(image, axis=0)

        predictions = self.model.predict(
            image,
            verbose=0
        )[0]

        results = {}

        for name, probability in zip(
            self.class_names,
            predictions
        ):
            results[name] = float(probability)

        return results


    def save(self, name):

        self.model.save(name + ".keras")

        info = {
            "class_names": self.class_names,
            "image_size": self.image_size
        }

        with open(name + ".json", "w") as file:
            json.dump(info, file)

        print(f"Saved {name}.keras")


    @classmethod
    def load(cls, name):

        classifier = cls()

        classifier.model = keras.saving.load_model(
            name + ".keras"
        )

        with open(name + ".json") as file:
            info = json.load(file)

        classifier.class_names = info["class_names"]
        classifier.image_size = tuple(info["image_size"])

        return classifier