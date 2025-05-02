#!/bin/bash
echo "Setting up Lehua 5.0 environment..."
python3 -m venv lehua_env
source lehua_env/bin/activate
pip install -r requirements.txt
echo "Lehua 5.0 core environment activated."
