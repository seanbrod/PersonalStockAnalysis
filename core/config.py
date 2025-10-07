#Sean Broderick
import json
import os
from dotenv import load_dotenv

load_dotenv()

with open('config.json', 'r') as f:
    cf = json.load(f)

#Producer
stocks = cf['prod']['stocks']
funds = cf['prod']['funds']

#DB
db_url = os.getenv('DB_URL')