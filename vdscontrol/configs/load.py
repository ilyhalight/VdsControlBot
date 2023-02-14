import os
from dotenv import load_dotenv

try:
    import tomllib
except ModuleNotFoundError:
    import toml as tomllib

def load_cfg():
    with open('./configs/settings.cfg', 'rb') as f:
        return tomllib.load(f)

def load_env():
    """Загружает .env файл"""
    dotenv_path = os.path.join(os.path.dirname(__file__), '.env')

    if os.path.exists(dotenv_path):
        load_dotenv(dotenv_path)
        return True
    return False