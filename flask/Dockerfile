FROM python:3.7.3

#Set work directory and copy current directory's files to work directory
WORKDIR /app
COPY . /app

#Update python libraries to meet requirements
RUN pip install -r requirements.txt

ENTRYPOINT [ "python" ]

CMD [ "flaskApp.py" ]
