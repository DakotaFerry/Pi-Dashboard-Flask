FROM python:3.8

RUN pip install pipenv

#Set work directory and copy current directory's files to work directory
WORKDIR /app
COPY . .

#Update python libraries to meet requirements
RUN pipenv install



ENV FLASK_APP flaskApp.py

CMD [ "pipenv", "run", "gunicorn", "-w", "1", "-b", "0.0.0.0:5000", "wsgi:app" ]
