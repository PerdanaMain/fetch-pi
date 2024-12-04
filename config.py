import os
from dotenv import load_dotenv # type: ignore

class Config:
    def __init__(self):
        load_dotenv()
        self.PIWEB_API_URL = os.getenv("PIWEB_API_URL")
        self.PIWEB_API_USER = os.getenv("PIWEB_API_USER")
        self.PIWEB_API_PASS = os.getenv("PIWEB_API_PASS")
        self.PIWEB_API_VERIFY = os.getenv("PIWEB_API_VERIFY")
    
