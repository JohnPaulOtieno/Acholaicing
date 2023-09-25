#!/bin/bash

# Define the path to your virtual environment
VENV_PATH="/home/shikamaru/Acholaicing/dev"

# Check if the virtual environment directory exists
if [ -d "$VENV_PATH" ]; then
    # Activate the virtual environment
    source "$VENV_PATH/bin/activate"
    echo "Virtual environment activated."
else
    echo "Virtual environment not found at $VENV_PATH. Please update the path."
fi
