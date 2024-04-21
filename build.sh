#!/bin/zsh
SCRIPT_DIR=$(dirname "$0")

# Change the working directory to the script's directory
cd "$SCRIPT_DIR" || exit

# Script to execute setuptools commands for a Python project
python -m unittest discover -s . -p "unit_test.py" 
# Function to display usage instructions

# Check if a command is provided
echo "Building the distribution package..."
python setup.py sdist bdist_wheel
        

echo "Press any key to exit..."
read -n 1 -s
exit 0


