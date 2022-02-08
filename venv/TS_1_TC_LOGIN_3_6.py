from selenium import webdriver
import xlrd
from Get_Test_Data import getDataOfTest

# ----------------------------------------------------------------------------------------------------------------------
# TS: Verify Amazon Login Functionality
# TC3&6: Enter Valid email address and valid password.
# TC_OUT: Successful signing in. Go to Main Screen.
# ----------------------------------------------------------------------------------------------------------------------
#print("there we are ...")
# Get my test cases values:
email_data = getDataOfTest(3, 1)
password_data = getDataOfTest(6, 1)

# ----------------------------------------------------------------------------------------------------------------------

driver = webdriver.Chrome(executable_path="C:\\Users\\Rolla\\Downloads\\chromedriver.exe" )
#driver.get("https://www.amazon.eg/")
driver.maximize_window()
driver.get("https://www.amazon.com/ap/signin?openid.pape.max_auth_age=0&openid.return_to=https%3A%2F%2Fwww.amazon.com%2Flog%2Fs%3Fk%3Dlog%2Bin%26ref_%3Dnav_signin&openid.identity=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.assoc_handle=usflex&openid.mode=checkid_setup&openid.claimed_id=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0&")
driver.find_element_by_id("ap_email").send_keys(email_data)
driver.find_element_by_id("continue").click()
driver.find_element_by_id("ap_password").send_keys(password_data)
driver.find_element_by_id("signInSubmit").click()
driver.find_element_by_id("ap-account-fixup-phone-skip-link").click()


driver.close()
# ----------------------------------------------------------------------------------------------------------------------





