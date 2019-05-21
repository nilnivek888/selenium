import time
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC

t0 = time.time()
# put url of shoes
url = 'https://www.farfetch.com/shopping/men/saint-laurent-classic-boat-shoes-item-14026957.aspx'
url2 = "http://www.footlocker.com/product/model:190074/sku:61428007/jordan-retro-1-high-og-mens/?cm"
# personal information
fname = "John"
lname = "Fakename"
street1 = "811 E Dayton Street"
street2 = "apt 111"
zip = "10001"
city_address = "New York City"
phone_num = "6083202928"
email = "nyc111@gmail.com"
state = "New York"
CCnumber = "4072 0400 1020 0343"
CCmonth = "09"
CCyear = "20"
CCcsv = "060"

cart_url = 'https://www.farfetch.com/checkout/basket.aspx'

profile = webdriver.FirefoxProfile()
profile.set_preference("javascript.enabled", True)
# disable images
profile.set_preference("permissions.default.image", 2)
# disable css
# profile.set_preference('permissions.default.stylesheet', 2)
# disable flash
profile.set_preference('dom.ipc.plugins.enabled.libflashplayer.so', 'false')

shoesize = 11
browser = webdriver.Firefox(profile)

print('Loading page...')

browser.get(url)
print('Successful!')
# size
print('Selecting size...')
time.sleep(0.5)
browser.find_element_by_xpath("//*[@id='sizesDropdown']").click()
browser.find_element_by_xpath("//div[@class='af6f3d '][@data-value='26']").click()
print('Successful!')
# add to cart
WebDriverWait(browser, 20).until(EC.element_to_be_clickable((By.XPATH, "//button[@data-tstid='addToBag']")))
print('Adding to cart...')
add_to_cart = browser.find_element_by_xpath("//button[@data-tstid='addToBag']")
add_to_cart.click()
print('Successful!')
time.sleep(1)
print('Going to cart...')
browser.get(cart_url)
print('Successful!')
print('Going to checkout...')
checkout = browser.find_element_by_id("BasketGoToCheckout")
checkout.click()
if len(browser.find_elements_by_id("GoToCheckoutAsGuest")) == 0:
    browser.find_element_by_xpath("//*[@id='email-input-registration']").send_keys(email)
    WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((
            (By.XPATH, "//button[@value='Continue']"))))
    browser.find_element_by_xpath("//button[@value='Continue']").click()
    WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((
            (By.XPATH, "(//div[@class='chooser'])[2]"))))
    browser.find_element_by_xpath("(//div[@class='chooser'])[2]").click()
    stateB = browser.find_element_by_xpath("//li[@class='chooser-item'][contains(., state)]")
    print(stateB.text)
    ActionChains(browser).move_to_element(stateB)
    stateB.click()

else: # popup
    browser.find_element_by_id("GoToCheckoutAsGuest").click()
    browser.find_element_by_xpath("/html/body/div[2]/main/section/div/div/div[1]/div[2]/div/section/div[1]/div/div/div/form/div[1]/div/div[8]/div[2]/div").click()
    stateB = browser.find_element_by_xpath("//li[@class='chooser-item'][contains(text(), state)]").click()
    ActionChains(browser).move_to_element(stateB).perform()

print('Successful!')

try:
    element = WebDriverWait(browser, 30).until(EC.visibility_of_element_located((By.ID, "FirstName")))
    print('Page loaded')
except TimeoutException:
    print('Page took too long to load')

print('Filling out shipping info')
browser.find_element_by_id("FirstName").send_keys(fname)
browser.find_element_by_id("LastName").send_keys(lname)
browser.find_element_by_id("StreetLine1").send_keys(street1)
browser.find_element_by_id("StreetLine2").send_keys(street2)
browser.find_element_by_id("PostalCode").send_keys(zip)
browser.find_element_by_id("AdministrativeArea").send_keys(city_address)
browser.find_element_by_xpath("/html/body/div[2]/main/section/div/div/div[1]/div[2]/div/section/div[1]/div/div/div/form/div[1]/div/div[6]/div[2]/div").click()

phone = browser.find_element_by_id("billHomePhone")
phone.send_keys(phone_num)
email = browser.find_element_by_id("billEmailAddress")
email.send_keys(email)

print('Successful!')
print('Skipping delivery options')
next_step = browser.find_element_by_id("billPaneContinue")

print('Button clicked')

try:
    next_step.click()
    # print("Use suggested address")
    # browser.find_element_by_xpath("/html//a[@id='address_verification_use_suggested_address']").click()
    element = WebDriverWait(browser, 300).until(
        EC.presence_of_element_located((By.ID, "shipMethod3")))
    print('Page passed')
    next_step_loaded = True
    print('Successful!')
    print('Loading next step')
    if next_step_loaded == True:
        next_step_2 = browser.find_element_by_id("shipMethodPaneContinue")
        next_step_2.click()
except TimeoutException:
    print('Page took too long to load')

try:
    element = WebDriverWait(browser, 300).until(
        EC.element_to_be_clickable((By.ID, "CardNumber")))
    print('Page loaded')
    credit_info_loaded = True
except TimeoutException:
    print('Page took too long to load')

if credit_info_loaded == True:
    time.sleep(3)
    print('Filling out credit card information')
    credit_card_number = browser.find_element_by_id("CardNumber")
    credit_card_number.send_keys(CCnumber)
    credit_card_number_month = browser.find_element_by_id("CardExpireDateMM")
    credit_card_number_month.send_keys(CCmonth)
    credit_card_number_year = browser.find_element_by_id("CardExpireDateYY")
    credit_card_number_year.send_keys(CCyear)
    credit_card_number_year = browser.find_element_by_id("CardCCV")
    credit_card_number_year.send_keys(CCcsv)
    print('Successful')
    next_step_3 = browser.find_element_by_id("payMethodPaneContinue")
    next_step_3.click()
# insert wait here
try:
    element = WebDriverWait(browser, 300).until(
        EC.element_to_be_clickable((By.ID, "orderReviewPaneBillSubscribeEmail")))
    print('Page loaded')
except TimeoutException:
    print('Page took too long to load')
email_promotions = browser.find_element_by_id("orderReviewPaneBillSubscribeEmail")
email_promotions.click()

print('clicked button')
t1 = time.time()
print(t1 - t0, end="")
print(" seconds")
