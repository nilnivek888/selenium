import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
t0 = time.time()
# put url of shoes
url = 'https://www.footlocker.com/product/item/2588006.html'
url2 = "http://www.footlocker.com/product/model:190074/sku:61428007/jordan-retro-1-high-og-mens/?cm"
# personal information
fname = "Kevin"
lname = "Lin"
street_address = "835 W Dayton Street"
zip = "53706"
city_address = "Madison"
phone_num = "6083202928"
email_address = "nilnivek888@yahoo.com.tw"

CCnumber = "4072 0400 1020 0343"
CCmonth = "09"
CCyear = "20"
CCcsv = "060"

# Do not change anything below this line
# shoe sizes
size6 = "//span[@id='size_selection_list']/a[@title='Size 6.0']"
size65 = "//span[@id='size_selection_list']/a[@title='Size 6.5']"
size7 = "//span[@id='size_selection_list']/a[@title='Size 7.0']"
size75 = "//span[@id='size_selection_list']/a[@title='Size 7.5']"
size8 = "//span[@id='size_selection_list']/a[@title='Size 8.0']"
size85 = "//span[@id='size_selection_list']/a[@title='Size 8.5']"
size9 = "//span[@id='size_selection_list']/a[@title='Size 9.0']"
size95 = "//span[@id='size_selection_list']/a[@title='Size 9.5']"
size10 = "//span[@id='size_selection_list']/a[@title='Size 10.0']"
size105 = "//span[@id='size_selection_list']/a[@title='Size 10.5']"
size11 = "//span[@id='size_selection_list']/a[@title='Size 11.0']"
size115 = "//span[@id='size_selection_list']/a[@title='Size 11.5']"
size12 = "//span[@id='size_selection_list']/a[@title='Size 12.0']"
size125 = "//span[@id='size_selection_list']/a[@title='Size 12.5']"

size18 = "//span[@id='size_selection_list']/a[@title='Size 18.0']"
chosen_size = size12

cart_url = 'http://www.footlocker.com/shoppingcart/default.cfm?sku='
shipping_info_loaded = False
credit_info_loaded = False
successful_load = False

profile = webdriver.FirefoxProfile()
profile.set_preference("javascript.enabled", True)
# disable images
profile.set_preference("permissions.default.image", 2)
# disable css
#profile.set_preference('permissions.default.stylesheet', 2)
# disable flash
profile.set_preference('dom.ipc.plugins.enabled.libflashplayer.so','false')

browser = webdriver.Firefox(profile)
print('Loading page...')

browser.get(url)
print('Successful!')
# size
print('Selecting size...')
browser.find_element_by_id('pdp_size_select_mask').click()
time.sleep(0.5)
browser.find_element_by_xpath(chosen_size).click()
print('Successful!')
# add to cart
print('Adding to cart...')
add_to_cart = browser.find_element_by_id("pdp_addtocart_button")
add_to_cart.click()
print('Successful!')
time.sleep(1)
print('Going to cart...')
browser.get(cart_url)
print('Successful!')
print('Going to checkout...')
checkout = browser.find_element_by_id("cart_checkout_button")
checkout.click()
print('Successful!')
print('Going to billing...')

# waits for page to load

try:
    element = WebDriverWait(browser, 300).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="billFirstName"]')))
    print('Page loaded')
    shipping_info_loaded = True
except TimeoutException:
    print('Page took too long to load')

if shipping_info_loaded == True:
    time.sleep(3)
    print('Filling out shipping info')
    first_name = browser.find_element_by_id("billFirstName")
    first_name.send_keys(fname)
    last_name = browser.find_element_by_id("billLastName")
    last_name.send_keys(lname)
    street = browser.find_element_by_id("billAddress1")
    street.send_keys(street_address)
    zipcode = browser.find_element_by_id("billPostalCode")
    zipcode.send_keys(zip)
    city = browser.find_element_by_id("billCity")
    city.send_keys(city_address)
    state = browser.find_element_by_id("billState")
    state.click()
    phone = browser.find_element_by_id("billHomePhone")
    phone.send_keys(phone_num)
    email = browser.find_element_by_id("billEmailAddress")
    email.send_keys(email_address)

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
print(t1-t0,end = "")
print(" seconds")
#browser.get('http://www.footlocker.com/shoppingcart/default.cfm?')
#browser.find_element_by_xpath('//*[@id="cart_checkout_button_bottom"]').click()