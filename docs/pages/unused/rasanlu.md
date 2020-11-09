---
# This top area is to give jekyll information about the page.
layout: page
---
# Rasa NLU
## Installation
There are multiple ways to install Rasa.  
If you have docker, you can run a Rasa-Server with:  
  
`docker run -it -v "$(pwd):/app" -p 5005:5005 rasa/rasa:latest-spacy-en run --enable-api`  
  
With this command you enable the api, so you can train your model via Rhasspy, but that was not supported in our Rhasspy version (v2.5.5).  
If you do not have docker you can install Rasa by following [these](https://rasa.com/docs/rasa/installation/) steps.  

## Training

You can find our script to train your model at `/src/rasaTrain.py`.  
This script will train a model based on the markdown-files in `./intents/` relative to the path of the script.  
Your model will be saved at `/src/models/default/`.  
To test this model you can run `/src/rasaPredict.py`.  
If you change the project-name in the train-script you have to change the name in the predict-script, too. (default: "Info-Projekt")  
For this two script you need Python 3.7 and have to install `rasa_nlu[tensorflow]` via pip.  

## Run a server

To run a server without docker, you can run the following command:
 
``python -m rasa_nlu.server -P 5005 --path models/default/ -c nlu_config.yml``  
or  
``nohup python3 -m rasa_nlu.server -P 5005 --path models/default/ -c nlu_config.yml &``  
*If you want to run your server in background.*

Make sure to change the directory of the model and the `nlu_config.yml`, to wherever you have your files located.  
You should find your server at [http://localhost:5005/](http://localhost:5005/).
