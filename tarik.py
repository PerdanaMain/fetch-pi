import requests
import warnings
from requests.auth import HTTPBasicAuth
from datetime import datetime, timedelta
from config import Config

warnings.filterwarnings("ignore")

# URL yang ingin diakses
tanggal = "2024-10-03 03:40:30.252"
tanggal = datetime.strptime(tanggal, "%Y-%m-%d %H:%M:%S.%f")

host = Config().PIWEB_API_URL

val = []
tgl = tanggal.strftime("%Y-%m-%d %H:%M:%S.%f")[:-3]
url = (f"{host}/streams/F1DPw1kUu10ziUaXEx2rIyo4pAAgwAAAS1RKQi1LSTAwLVBJMVxUSkIzLkNPTkRSIFZBQyBQTVAgQSBTRVAgVEsgTFZM/value")

# Username dan Password
username = Config().PIWEB_API_USER
password = Config().PIWEB_API_PASS

# Nonaktifkan verifikasi SSL
try:
  response = requests.get(
    url, auth=HTTPBasicAuth(username, password), verify=False
  ).json()
  val.append(response)

except requests.exceptions.SSLError as e:
  print(f"SSL Error: {e}")
except Exception as e:
  print(f"Error: {e}")


print(val)