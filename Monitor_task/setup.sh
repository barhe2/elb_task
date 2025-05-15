#!/bin/bash
# This script creates a virtual environment, activates it based on OS,
# installs dependencies, and runs app.py. OS detection is simplified
# to the command needed for venv activation.

# 1. Create a virtual environment named 'cpu'
echo "Creating virtual environment named 'cpu'"
python3 -m venv cpu
if [ $? -ne 0 ]; then
  echo "Error creating the virtual environment."
  exit 1
fi

# 2. Attempt to activate the virtual environment based on common paths
echo "Attempting to activate the virtual environment..."

# Try Linux/macOS activation
if [ -f "cpu/bin/activate" ]; then
  source cpu/bin/activate
  VENV_ACTIVATED=true
fi

# If not activated, try Windows activation
if [ -z "$VENV_ACTIVATED" ] && [ -f "cpu/Scripts/activate" ]; then
  source cpu/Scripts/activate
  VENV_ACTIVATED=true
fi

# If still not activated, inform the user and exit
if [ -z "$VENV_ACTIVATED" ]; then
  echo "Could not automatically activate the virtual environment."
  echo "Please ensure the virtual environment was created successfully."
  exit 1
fi

echo "Activated the virtual environment 'cpu'."

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

# 4. Run the app.py script
if [ -f "app.py" ]; then
  echo "Running the app.py script..."
  python app.py
  if [ $? -ne 0 ]; then
    echo "Error running app.py."
  fi
else
  echo "app.py file not found."
fi

# Deactivate the virtual environment upon completion (optional)
deactivate
echo "Deactivated the virtual environment."

exit 0