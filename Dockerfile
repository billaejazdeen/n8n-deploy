# Start from the official n8n Alpine-based image
FROM n8nio/n8n:latest

# Switch to root user to install packages
USER root

# Install system dependencies for Python and Chromium
# Combining RUN commands reduces Docker image layers
RUN apk update && apk add --no-cache \
    python3 \
    py3-pip \
    chromium \
    chromium-chromedriver

# Install required Python packages globally
# We remove webdriver-manager as it's no longer needed
RUN pip install --no-cache-dir pandas numpy openpyxl selenium

# Set the PATH to include the Chromium browser executable
ENV PATH=$PATH:/usr/lib/chromium/

# Switch back to the non-root node user
USER node

# Copy your Python scripts into the n8n user's home directory
COPY scripts/py-n8n.py /home/node/py-n8n.py
COPY scripts/facebook.py /home/node/facebook.py