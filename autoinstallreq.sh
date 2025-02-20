#!/bin/bash

# Prompt user for confirmation
echo "This script will install the following components:"
echo "1. Update and upgrade the system packages"
echo "2. Install Python3 and pip"
echo "3. Install Ollama"
echo "4. Download CodeLlama from Ollama"
echo "5. Install dependencies for Python3"
echo
read -p "Do you want to continue? (y/n): " choice

# Convert input to lowercase for consistency
choice=$(echo "$choice" | tr '[:upper:]' '[:lower:]')

if [[ "$choice" != "y" ]]; then
    echo "Installation aborted by user."
    exit 1
fi

# Update package list and upgrade packages
echo "Updating package list..."
sudo apt update && sudo apt upgrade -y

# Install Python and pip (if not installed)
echo "Checking and installing Python and pip..."
sudo apt install -y python3 python3-pip

# Installing Ollama
echo "Installing Ollama..."
curl -fsSL https://ollama.com/install.sh | sh

# Pulling CodeLlama from Ollama
echo "Downloading CodeLlama from Ollama."
echo "This may take a while depending on your internet speed..."
ollama pull codellama

# Install requirements
if [ -f "requirements.txt" ]; then
    echo "Installing dependencies from requirements.txt..."
    pip install -r requirements.txt
else
    echo "No requirements.txt found. Skipping dependency installation."
fi

# Final message
echo "Installation complete!"
echo "Simply run 'python3 aiterminal.py' to get started!"
