FROM python:3
ENV PYTHONUNBUFFERED 1

RUN mkdir /app
WORKDIR /app
COPY requirements.txt /app/
EXPOSE 5000
RUN pip install -r requirements.txt
ENV FLASK_ENV="docker"
COPY . /app/
CMD python app.py