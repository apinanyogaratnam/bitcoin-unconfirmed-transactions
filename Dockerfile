FROM python:3.10-alpine3.17

WORKDIR /app

# copy dependency list
COPY Pipfile Pipfile.lock ./
COPY Makefile /app/Makefile

# install make
RUN apk add make

# install dependencies
RUN make install

# copy the rest of the files
COPY . .

CMD ["pipenv", "run", "python", "main.py"]
