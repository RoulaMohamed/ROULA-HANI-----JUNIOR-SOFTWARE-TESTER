from selenium import webdriver
import xlrd
from Get_Test_Data import getDataOfTest
from subprocess import call
import os

# ----------------------------------------------------------------------------------------------------------------------
# TS: Verify Amazon Login Functionality
# TC3&6: Enter Valid email address and valid password.
# TC_OUT: Successful signing in. Go to Main Screen.
# ----------------------------------------------------------------------------------------------------------------------
def run(runfile):
  with open(runfile,"r") as rnf:
    exec(rnf.read())
# ----------------------------------------------------------------------------------------------------------------------
# Get my test cases values:
search_data = getDataOfTest(3, 0)

# ----------------------------------------------------------------------------------------------------------------------

#call(["python", "TS_2_TC_SEARCH_3_6.py"])
run('TS_1_TC_LOGIN_3_6.py')
print(search_data)
driver = webdriver.Chrome(executable_path="C:\\Users\\Rolla\\Downloads\\chromedriver.exe" )
driver.maximize_window()
#driver.implicitly_wait(10)
#driver.get("https://www.amazon.com/ap/signin?openid.pape.max_auth_age=0&openid.return_to=https%3A%2F%2Fwww.amazon.com%2Flog%2Fs%3Fk%3Dlog%2Bin%26ref_%3Dnav_signin&openid.identity=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.assoc_handle=usflex&openid.mode=checkid_setup&openid.claimed_id=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0&")
driver.find_element_by_id("twotabsearchtextbox").send_keys(search_data)
driver.find_element_by_id("nav-search-submit-button").click()
driver.find_element_by_id("p13n-asin-index-0").click()


driver.close()
# ----------------------------------------------------------------------------------------------------------------------