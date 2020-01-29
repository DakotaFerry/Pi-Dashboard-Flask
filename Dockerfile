FROM python:3.8

RUN pip install pipenv

#Set work directory and copy current directory's files to work directory
WORKDIR /app
COPY . .

#Prevent python from writing pyc files to disk or buffering stdout and stderr 
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

#Update python libraries to meet requirements
RUN pipenv install

CMD [ "pipenv", "run", "gunicorn", "-w", "1", "-b", ":5000", "wsgi:app" ]
