from time import sleep
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import re
from bs4 import BeautifulSoup as bs
from random import randint

# Sleep Intervals
## 1 Sec - Post Data Entry
## 2 Sec - Post DOM update
## 3 Sec - New page rendered

def start_browser():
    driver = webdriver.Firefox()
    sleep(5)
    return driver

def login(driver, username, password):
    driver.get('https://www.linkedin.com')
    element = driver.find_element_by_xpath('//*[@id="login-email"]')
    element.send_keys(username)
    sleep(1)
    element = driver.find_element_by_xpath('//*[@id="login-password"]')
    element.send_keys(password)
    sleep(1)
    driver.find_element_by_xpath('//*[@id="login-submit"]').click()
    sleep(5)
    html = driver.page_source
    if "My Network" in html:
        return True
    else:
        return False

def get_phish_targets(driver, company):
    # Enter company name in search field and click Enter
    element = driver.find_element_by_xpath('/html/body/nav/div/form/div/div/div/artdeco-typeahead-deprecated/artdeco-typeahead-deprecated-input/input')
    element.send_keys(company)
    sleep(1)
    element.send_keys(Keys.ENTER)
    sleep(5)
    # Click the People Banner to narrow to Profiles
    try:
        driver.find_element_by_xpath('/html/body/div[5]/div[5]/div[2]/div/div[1]/div/div/nav/div[1]/ul/li[1]/button').click()
    except:
        sleep(10)
        driver.find_element_by_xpath('/html/body/div[5]/div[5]/div[2]/div/div[1]/div/div/nav/div[1]/ul/li[1]/button').click()
    sleep(10)
    # Open Advanced Search Filters
    try:
        driver.find_element_by_xpath('/html/body/div[5]/div[5]/div[2]/div/div[1]/div/div/nav/div[2]/button').click()
    except:
        sleep(10)
        driver.find_element_by_xpath('/html/body/div[5]/div[5]/div[2]/div/div[1]/div/div/nav/div[2]/button').click()
    sleep(5)
    # Define Current Company
    try:
        driver.find_element_by_xpath('/html/body/div[1]/artdeco-modal-overlay/artdeco-modal/artdeco-modal-content/div/div[1]/ul/li[6]/form/div[2]/fieldset/ol/li[2]/label').click()
    except:
        sleep(10)
        driver.find_element_by_xpath('/html/body/div[1]/artdeco-modal-overlay/artdeco-modal/artdeco-modal-content/div/div[1]/ul/li[6]/form/div[2]/fieldset/ol/li[2]/label').click()
    sleep(2)
    # Define Technology Industry
    '''
    try:
        driver.find_element_by_xpath('/html/body/div[1]/artdeco-modal-overlay/artdeco-modal/artdeco-modal-content/div/div[1]/ul/li[8]/form/div[2]/fieldset/ol/li[3]/label').click()
    except:
        sleep(10)
        driver.find_element_by_xpath('/html/body/div[1]/artdeco-modal-overlay/artdeco-modal/artdeco-modal-content/div/div[1]/ul/li[8]/form/div[2]/fieldset/ol/li[3]/label').click()
    sleep(2)
    '''
    # Apply Filters
    driver.find_element_by_xpath('/html/body/div[1]/artdeco-modal-overlay/artdeco-modal/artdeco-modal-header/div/div[2]/button[2]').click()
    sleep(10)
    # Scroll Down to Render All Profiles
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    sleep(3)
    # Pull Source and Search for Profile Names
    html = driver.page_source
    soup = bs(html, 'html.parser')
    regex = r'(?<=<span class="name actor-name">)[A-Za-z][A-Za-z]+ [A-Za-z][A-Za-z]+'
    results = re.findall(regex, str(soup))
    phishtargets = []
    for result in results:
        print result
        phishtargets.append(result)
    randsleep = randint(10, 40)
    print "    [+] Sleeping for " + str(randsleep) + " seconds to avoid bot detection"
    sleep(randsleep)
    try:
        driver.find_element_by_xpath('/html/body/div[5]/div[5]/div[2]/div/div[2]/div[1]/div/div[2]/div/div/div/div/div/div[1]/ol/li[2]/button').click()
    except:
        sleep(10)
        driver.find_element_by_xpath('/html/body/div[5]/div[5]/div[2]/div/div[2]/div[1]/div/div[2]/div/div/div/div/div/div[1]/ol/li[2]/button').click()
    for x in range(2, 100):
        sleep(6)
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        sleep(3)
        html = driver.page_source
        soup = bs(html, 'html.parser')
        regex = r'(?<=<span class="name actor-name">)[A-Za-z][A-Za-z]+ [A-Za-z][A-Za-z]+'
        results = re.findall(regex, str(soup))
        for result in results:
            print result
            phishtargets.append(result)
        randsleep = randint(10, 40)
        print "    [+] Sleeping for " + str(randsleep) + " seconds to avoid bot detection"
        sleep(randsleep)
        driver.find_element_by_xpath('/html/body/div[5]/div[5]/div[2]/div/div[2]/div[1]/div/div[2]/div/div/div/div/div/div[1]/ol/li[3]/button').click()
        sleep(3)
    return phishtargets
