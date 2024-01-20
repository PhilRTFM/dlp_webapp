#!/bin/bash

# Check for Homebrew and install it if it's not installed
if ! command -v brew &> /dev/null
then
    echo "Installing Homebrew..."
    /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
fi

# Install Python
echo "Installing Python..."
brew install python

# Navigate to the app directory (replace with actual directory name)
cd /path/to/your/app/directory

# Install Flask and other dependencies
echo "Installing dependencies..."
pip3 install -r requirements.txt

echo "Installation completed."
