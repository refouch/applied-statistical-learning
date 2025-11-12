import os 
import hashlib

# ==== Defining paths ====
ROOT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
checksum_path = os.path.join(ROOT_DIR, "data/fma_metadata/checksums")
data_path = os.path.join(ROOT_DIR,"data/fma_metadata")

def sha1sum(filepath) -> str:
    """Function to calculate the sha1 hash of a given file"""
    h = hashlib.sha1()
    with open(filepath, "rb") as f:
        for chunk in iter(lambda: f.read(8192), b""):
            h.update(chunk)
    return h.hexdigest()


def retrieve_checksums() -> dict:
    """Function storing every checksum from the dataset integrity file in a dictionnary"""
    checksums = {}
    with open(checksum_path, "r") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            sha1, filename = line.split(maxsplit=1)
            checksums[filename] = sha1
    return checksums


def check_integrity() -> bool:
    """Function to check the dataset integrity.
        Returns:
            - True if all file's hash corresponds to the given checksums
            - False is at least one file is corrupted or missing"""

    print("Checking the dataset integrity...")

    checksums = retrieve_checksums()

    for filename, expected_sha1 in checksums.items():
        file_path = os.path.join(data_path, filename)

        if not os.path.exists(file_path):
            print(f"Missing file : {filename}")
            return False

        actual_sha1 = sha1sum(file_path)
        if actual_sha1 == expected_sha1:
            print(f"{filename}: OK")
        else:
            print(f"  {filename} CORRUPTED !")
            print(f"   Expected : {expected_sha1}")
            print(f"   Found  : {actual_sha1}")
            return False
        
    return True

if __name__ == "__main__":
    check_integrity()