FROM python:3.12-slim

ENV PYTHONUNBUFFERED=1
WORKDIR /usr/src/app
COPY crawler.py .
COPY poster.py .
COPY requirements.txt ./
RUN pip install -r requirements.txt

RUN groupadd --gid 1000 user && \
    useradd --uid 1000 --gid 1000 --create-home --shell /bin/bash user

RUN chown -R "1000:1000" /home/user
USER user

CMD tail -f /dev/null