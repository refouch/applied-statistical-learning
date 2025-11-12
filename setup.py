"""
Script to automate installing the necessary dependencies and downloading the dataset.
Automatically run at the beggining of the main notebook.
"""

import os
import shutil

ROOT_DIR = os.path.dirname(__file__)
dataset_dir = os.path.join(ROOT_DIR, "data", "fma_metadata")

# ======= Dataset integrity and download ======
from utils.check_data_integrity import check_integrity
from utils.download_dataset import download_and_extract

print('Checking the dataset existence and integrity.')

path_exists = os.path.exists(dataset_dir)
integrity = check_integrity() if path_exists else False

if not integrity:
    print("Dataset does not exist or is corrupted. Downloading again...")
    if path_exists:
        shutil.rmtree(dataset_dir)
    download_and_extract()
else:
    print("Dataset exists and is intact.")


# ======= venv and dependencies ======
import subprocess
import venv

print("Installing dependencies")

venv_dir = os.path.join(ROOT_DIR, "env")
requirements_file = os.path.join(ROOT_DIR, "requirements.txt")

if not os.path.exists(venv_dir):
    print("Creating a new virtual environment...")
    venv.create(venv_dir, with_pip=True)
else:
    print("Virtual environment already exists")

if os.name == "nt":  # Windows
    python_bin = os.path.join(venv_dir, "Scripts", "python.exe")
else:  # Unix / MacOS
    python_bin = os.path.join(venv_dir, "bin", "python")

print("Installing dependancies from requirements.txt...")
subprocess.check_call([python_bin, "-m", "pip", "install", "--upgrade", "pip"])
subprocess.check_call([python_bin, "-m", "pip", "install", "-r", requirements_file])

print("All dependencies installed.")