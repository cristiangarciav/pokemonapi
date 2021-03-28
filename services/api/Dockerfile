# Pulling the official base image
FROM python:3.7-alpine

# Setting environment variables
ENV PROJECTPATH /usr/src/app
ENV PYTHONPATH ${PROJECTPATH}
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBURRERED 1

# Setting working directory
WORKDIR ${PROJECTPATH}

# Installing dependencies
RUN pip install pipenv
COPY ./Pipfile ./Pipfile.lock ${PROJECTPATH}/
RUN pipenv install --system --deploy

COPY ./ ${PROJECTPATH}
RUN adduser -D pythonuser
USER pythonuser
CMD ["sh", "-c", "gunicorn --bind 0.0.0.0:5000 manage:app"]
