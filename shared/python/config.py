import os
from dotenv import load_dotenv

# Cargar las variables de entorno desde el archivo .env
load_dotenv()

# Variables de configuración centralizadas
DB_ADDRESS = os.getenv("DB_ADDRESS")
BASE_URL_GET_INSTITUTIONS = os.getenv('BASE_URL_GET_INSTITUTIONS')
API_KEY_ID = os.getenv('API_KEY_ID')
API_KEY_SECRET = os.getenv('API_KEY_SECRET')
BASE_URL_ACCOUNT_ID = os.getenv('BASE_URL_ACCOUNT_ID')