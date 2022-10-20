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
        def is_within_directory(directory, target):
            
            abs_directory = os.path.abspath(directory)
            abs_target = os.path.abspath(target)
        
            prefix = os.path.commonprefix([abs_directory, abs_target])
            
            return prefix == abs_directory
        
        def safe_extract(tar, path=".", members=None, *, numeric_owner=False):
        
            for member in tar.getmembers():
                member_path = os.path.join(path, member.name)
                if not is_within_directory(path, member_path):
                    raise Exception("Attempted Path Traversal in Tar File")
        
            tar.extractall(path, members, numeric_owner=numeric_owner) 
            
        
        safe_extract(tgz_file, path=os.path.join(BASE_PATH,"data"))
