import os
import tarfile
import urllib

from src.constant import BASE_PATH

DOWNLOAD_ROOT: str = "https://raw.githubusercontent.com/ageron/handson-ml2/master/"


def fetch_tgz_data(path: str) -> None:
    file_path = os.path.join(DOWNLOAD_ROOT, "datasets", path)
    tgz_destination_path = os.path.join(BASE_PATH, "data", os.path.split(path)[1])

    urllib.request.urlretrieve(url=file_path, filename=tgz_destination_path)

    with tarfile.open(tgz_destination_path) as tgz_file:
        tgz_file.extractall(path=os.path.join(BASE_PATH, "data"))
