Step1: 

     console: docker-compose up -d --build
     console: docker-compose exec -u root chat_app bash

Step2: 

    console: pdm runserver

Step3: 

    web: http://localhost:8000/

step4:

    git config --global --add safe.directory /home/python/app

step5:

    chmod +x .docker/start-app.sh
