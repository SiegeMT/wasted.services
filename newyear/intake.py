#%%
from bs4 import BeautifulSoup
import param
import panel
import requests


item_request_headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1985.125 Safari/537.36",
    "Accept": "*/*",
    "Accept-Encoding": "gzip,deflate,sdch",
    "Accept-Language": "en-US,en;q=0.8",
}
#%%
#payload = { "dnn_ctr46796_Default_List_txtSearch": "NOTE 1500" }

payload = { "": "NOTE 1500" }
session = requests.Session()

session.headers = item_request_headers


form_response = session.get(
    url='https://www.med.navy.mil/Directives/Notices/', params=payload)

soup = BeautifulSoup(form_response.content)
#%%
callbackid = soup.select('input[name=__CALLBACKID]')[0]['value']


item_url = 'http://www.example.com/EN/items/Pages/yourrates.aspx'

response = session.post(
    url=item_url, 
    params=payload, 
    data=item_request_body, 
    headers={'Referer': form_response.url})
# %%
