You can see the project live on www.calculatorpro.co

To see project from localhost:8000, please start with installing Docker Engine and Docker Compose.

https://docs.docker.com/engine/install/ubuntu/


Then run the following commands:

cd calculator_logs

docker-compose build

docker-compose up

_________________________________________________________________

Alternatively, you can run the project using a virtual environment:

cd calculator_logs/app

virtualenv venv

source venv/bin/activate

pip3 install -r requirements.txt

python3 manage.py migrate

python3 manage.py runserver
