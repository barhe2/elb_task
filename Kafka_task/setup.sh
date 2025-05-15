#!/bin/bash
# This script creates a virtual environment, activates it based on OS,
# installs dependencies.

# 1. Create a virtual environment named 'kafka_venv'
echo "Creating virtual environment named 'kafka_venv'"
python3 -m venv kafka_venv
if [ $? -ne 0 ]; then
  echo "Error creating the virtual environment."
  exit 1
fi

# 2. Attempt to activate the virtual environment based on common paths
echo "Attempting to activate the virtual environment..."

# Try Linux/macOS activation
if [ -f "kafka_venv/bin/activate" ]; then
  source kafka_venv/bin/activate
  VENV_ACTIVATED=true
fi

# If not activated, try Windows activation
if [ -z "$VENV_ACTIVATED" ] && [ -f "kafka_venv/Scripts/activate" ]; then
  source kafka_venv/Scripts/activate
  VENV_ACTIVATED=true
fi

# If still not activated, inform the user and exit
if [ -z "$VENV_ACTIVATED" ]; then
  echo "Could not automatically activate the virtual environment."
  echo "Please ensure the virtual environment was created successfully."
  exit 1
fi

echo "Activated the virtual environment 'kafka_venv'."

# 3. Install dependencies from requirements.txt
if [ -f "requirements.txt" ]; then
  echo "Installing packages from requirements.txt..."
  pip install -r requirements.txt
  if [ $? -ne 0 ]; then
    echo "Error installing packages."
    deactivate
    exit 1
  fi
else
  echo "requirements.txt file not found."
fi

exit 0