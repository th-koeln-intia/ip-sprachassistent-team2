from rasa_nlu.training_data import load_data
from rasa_nlu import config
from rasa_nlu.model import Trainer


def train(model_dir="./models", project="default", data_dir="./intents"):
    training_data = load_data(data_dir)
    trainer = Trainer(config.load("nlu_config.yml"))
    trainer.train(training_data)
    model_directory = trainer.persist(model_dir, fixed_model_name=project)
    print(model_directory)


if __name__ == '__main__':
    train(project="Info-Projekt")
