FROM python:3.8


# https://stackoverflow.com/questions/59812009/what-is-the-use-of-pythonunbuffered-in-docker-file/59812588
ENV PYTHONUNBUFFERED 1

# RUN mkdir /code
WORKDIR /code


# RUN apk add --update --no-cache postgresql-client jpeg-dev gettext redis mysql mysql-client
# RUN apk update \
#     && apk add --virtual build-deps gcc python3-dev musl-dev \
#     && apk add --no-cache mariadb-dev
# RUN apk add --update --no-cache --virtual .tmp-build-deps \
#     gcc libc-dev linux-headers postgresql-dev musl-dev zlib zlib-dev libffi-dev openssl-dev git mysql-client
#
#RUN pip install psycopg2-binary



# Adding environment variables
# COPY .env /code/

# Installing requirements
COPY requirements.txt /code/
RUN pip install --no-cache-dir -r requirements.txt
# Setting entrypoint
COPY . /code/
COPY entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

COPY . /code/

EXPOSE 8000

# run entrypoint.sh
ENTRYPOINT ["/entrypoint.sh"]