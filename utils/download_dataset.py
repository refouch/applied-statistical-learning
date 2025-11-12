import os
from urllib.request import urlretrieve
import zipfile
import sys

# ====== PATH and URLs ======
FMA_url = "https://os.unil.cloud.switch.ch/fma/fma_metadata.zip"
ROOT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
data_path = os.path.join(ROOT_DIR, "data")
zip_path = os.path.join(data_path,"fma_metadata.zip")


def progress_bar(block_num, block_size, total_size):
    """Hook for urllib.request.urlretrieve to print a download progress bar"""
    downloaded = block_num * block_size
    percent = min(100, downloaded * 100 / total_size)
    bar_len = 40
    filled_len = int(bar_len * percent / 100)
    bar = "█" * filled_len + "-" * (bar_len - filled_len)
    sys.stdout.write(f"\rDownload: |{bar}| {percent:5.1f}%")
    sys.stdout.flush()
    if downloaded >= total_size:
        print() 

def download_dataset():
    """Simple call to urlib in order to download the dataset zip file in the right folder."""
    print(f"Started downloading dataset from {FMA_url}...")
    urlretrieve(FMA_url,zip_path,reporthook=progress_bar)
    print("Dowload Finished !")

def unzip_dataset():
    """Simple function to unzip and delete the dowloaded archive"""
    print("Unzipping files...")
    with zipfile.ZipFile(zip_path, 'r') as zip:
        zip.extractall(data_path)
    print(f"Files extracted in the following folder: {data_path}/fma_metadata")
    os.remove(zip_path)

def download_and_extract():
    """main function."""
    download_dataset()
    unzip_dataset()

if __name__ == "__main__":
    download_and_extract()