from selenium import webdriver
import xlrd
from Get_Test_Data import getDataOfTest

i = 1
testCases = 2
# Check test case 3 and 6
# Then ceck test case 3 and 5
test_cases_combination = [3 , 6, 3 , 5]

driver = webdriver.Chrome(executable_path="C:\\Users\\Rolla\\Downloads\\chromedriver.exe")
# driver.get("https://www.amazon.eg/")
driver.maximize_window()
driver.get(
    "https://www.amazon.com/ap/signin?openid.pape.max_auth_age=0&openid.return_to=https%3A%2F%2Fwww.amazon.com%2Flog%2Fs%3Fk%3Dlog%2Bin%26ref_%3Dnav_signin&openid.identity=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.assoc_handle=usflex&openid.mode=checkid_setup&openid.claimed_id=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0&")

while i < testCases:
    email_data = getDataOfTest(test_cases_combination[i-1])
    #email_data = "w@sw"
    password_data = getDataOfTest(test_cases_combination[i])

    driver.find_element_by_id("ap_email").send_keys(email_data)

    driver.find_element_by_id("continue").click()

    BIAdisplayed = driver.get_attribute("ap_email")
    if BIAdisplayed == "0":
        raise Exception('test case ' + i + ' fails')
        continue

    driver.find_element_by_id("ap_password").send_keys(password_data)
    driver.find_element_by_id("signInSubmit").click()

    BIAdisplayed2 = driver.get_attribute("ap_password")
    if BIAdisplayed2 == "0":
        raise Exception('test case ' + (i+1) + ' fails')
        continue


    driver.find_element_by_id("ap-account-fixup-phone-skip-link").click()

driver.close()

