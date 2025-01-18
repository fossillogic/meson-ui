FROM debian:bullseye

RUN apt-get update && apt-get install -y \
    python3 \
    python3-pip \
    git \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app
COPY . /app

RUN pip3 install -r requirements.txt

CMD ["python", "./meson-ui.py"]