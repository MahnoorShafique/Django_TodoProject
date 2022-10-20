FROM python:3.9
# to show errors on terminal in docker lof files
ENV PYTHONUNBUFFERED=1
WORKDIR /django
COPY todo_app/requirements/base.txt requirements.txt
RUN pip3 install -r requirements.txt