import psycopg2
from config import load_config
from connect import get_contacts, get_contacts_phone
from connect import connect

# Connect to the server
config = load_config()
connect(config)

get_contacts()
get_contacts_phone()



