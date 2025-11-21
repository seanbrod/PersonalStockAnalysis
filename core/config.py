#Sean Broderick
import json
import os
from dotenv import load_dotenv

load_dotenv()

#Producer
s_set = {"PLTR", "RTX", "META", "GOOGL"}
f_set = {"VOO", "SWPPX", "SPYD", "SCHX", "SCHD", "SCHA"}
stocks = " ".join(s_set)
funds = " ".join(f_set)

#TODO: have some dict or other DS that holds the individual stocks or funds so we can quickly check if an ID is a stock or fund

#DB
db_url = os.getenv('DB_URL')