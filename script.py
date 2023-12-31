import subprocess
import time

def run_script(file_name):
    try:
        subprocess.run(["python", file_name], check=True)
        print(f"{file_name} executed successfully.")
    except subprocess.CalledProcessError as e:
        print(f"Error occurred while executing {file_name}: {e}")

if __name__ == "__main__":
    files_to_run = ["LRUcache.py", "LRUSEEcache.py", "FIFOcache.py", "FIFOSEEcache.py"]

    for file in files_to_run:
        run_script(file)