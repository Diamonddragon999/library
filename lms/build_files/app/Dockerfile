FROM python:3.10-slim-bullseye


COPY app/requirements.txt .
RUN apt update; apt install pkg-config python3-dev default-libmysqlclient-dev build-essential -y
RUN pip install --no-cache-dir -r requirements.txt

RUN useradd -d /home/lsm_admin/ -m -p lsm_admin -s /bin/bash lsm_admin
RUN echo "lsm_admin:89hfweh89efhwwfhew9ehf8whe89fwhwehwehf9wgf9ewef" | chpasswd 
COPY ./app /home/lsm_admin/app
WORKDIR /home/lsm_admin/app
USER lsm_admin

ENTRYPOINT [ "python3", "-m", "flask", "run", "--host", "0.0.0.0", "--port","4443" ]
# ENTRYPOINT [ "python3", "app.py" ]
