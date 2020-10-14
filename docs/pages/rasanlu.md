---
# This top area is to give jekyll information about the page.
layout: default
---

``docker run -it -v "$(pwd):/app" -p 5005:5005 koenvervloesem/rasa:latest``

``python -m rasa_nlu.server -P 5005 --path models/default/ -c nlu_config.yml``  

``nohup python3 -m rasa_nlu.server -P 5005 --path models/default/ -c nlu_config.yml &``
