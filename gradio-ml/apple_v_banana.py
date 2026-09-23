from modules import ImageClassifier

model = ImageClassifier("datasets/fruit")

model.train()

print(model.predict("test_fruit.jpg"))