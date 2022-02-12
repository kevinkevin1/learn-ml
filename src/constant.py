import os
from pathlib import Path

BASE_PATH = str(Path(__file__).parent.parent)
USER_NAME = os.getenv("USER").lower()
