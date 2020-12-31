from rasa_nlu.model import Interpreter


def predict(text="hi", model_dir="./models/default", project="default"):
    interpreter = Interpreter.load(model_dir + "/" + project)
    prediction = interpreter.parse(text)
    print(prediction)


if __name__ == '__main__':
    text = input()
    predict(text=text, project="Info-Projekt")
