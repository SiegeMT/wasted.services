#%%
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options


options=Options()
options.headless = True 
# %%
driver = webdriver.Firefox(options=options)
#%%
driver.get('https://ntmpsweb.dc3n.navy.mil/FLTMPS/DoDBanner.aspx')

# %%
class="ui-datepicker-title"
data-handler="selectMonth"
selectMonth.option

<select class="ui-datepicker-year" data-handler="selectYear" data-event="change">
<option value="2022" selected="selected">2022</option>


data-month=list(range(11))
data-year=[2021, 2022]