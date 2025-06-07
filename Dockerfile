FROM n8nio/n8n:latest

USER root

# Update and install python, chromium, chromedriver, and dependencies for Selenium
RUN apk update && apk add --no-cache \
    python3 py3-pip py3-virtualenv \
    chromium chromium-chromedriver \
    bash \
    nss \
    freetype \
    harfbuzz \
    ttf-freefont \
    fontconfig

ENV VENV_PATH=/opt/venv
RUN python3 -m venv $VENV_PATH

ENV PATH="$VENV_PATH/bin:$PATH"

# Install Python packages including selenium and webdriver-manager inside virtual environment
RUN $VENV_PATH/bin/pip install --no-cache-dir pandas numpy openpyxl selenium webdriver-manager

# Copy your selenium script from scripts folder to container
COPY scripts/py-n8n.py /home/node/py-n8n.py

# Set environment variables so Selenium knows where to find chromium
ENV CHROME_BIN=/usr/bin/chromium-browser
ENV PATH=$PATH:/usr/lib/chromium/

USER node
