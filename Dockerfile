FROM n8nio/n8n:latest

USER root

RUN apk update && apk add --no-cache python3 py3-pip py3-virtualenv

ENV VENV_PATH=/opt/venv
RUN python3 -m venv $VENV_PATH

ENV PATH="$VENV_PATH/bin:$PATH"

# Install pandas and numpy inside the virtual environment in one RUN command
RUN $VENV_PATH/bin/pip install --no-cache-dir pandas numpy openpyxl

USER node
# ✅ Copy your script from scripts folder into Docker container
COPY scripts/py-n8n.py /home/node/py-n8n.py