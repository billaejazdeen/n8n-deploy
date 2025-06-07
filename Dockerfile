# Start from the official n8n Alpine-based image
FROM n8nio/n8n:latest

# Switch to root user to install packages
USER root

# --- STEP 1: Install system dependencies AND build tools ---
# build-base and python3-dev are CRITICAL for installing numpy/pandas
RUN apk update && apk add --no-cache \
    python3 \
    py3-pip \
    chromium \
    chromium-chromedriver \
    build-base \
    python3-dev

# --- STEP 2: Create a virtual environment ---
ENV VENV_PATH=/home/node/venv
# Create the venv directory and change its ownership to the 'node' user
RUN mkdir -p $VENV_PATH && chown node:node $VENV_PATH

# Switch to the node user to create and use the venv
USER node
RUN python3 -m venv $VENV_PATH

# --- STEP 3: Activate the venv for subsequent commands and install packages ---
# This ensures 'pip' and 'python' commands use the venv
ENV PATH="$VENV_PATH/bin:$PATH"

# Install required Python packages into the venv
RUN pip install --no-cache-dir pandas numpy openpyxl selenium

# --- STEP 4: Copy your Python scripts ---
# This can be done after the environment is fully set up
COPY scripts/py-n8n.py /home/node/py-n8n.py
COPY scripts/facebook.py /home/node/facebook.py

# The container will continue to run as the 'node' user
# with the venv's PATH active for the Execute Code node.