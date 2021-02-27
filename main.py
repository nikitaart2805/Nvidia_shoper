import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

options = Options()
options.add_argument("--headless")
options.add_argument("window-size=1400,1500")
options.add_argument("--disable-gpu")
options.add_argument("--no-sandbox")
options.add_argument("start-maximized")
options.add_argument("enable-automation")
options.add_argument("--disable-infobars")
options.add_argument("--disable-dev-shm-usage")
browser = webdriver.Chrome('/usr/bin/chromedriver')

# BestBuy RTX 3060 Ti webpage
browser.get('https://www.bestbuy.com/site/amana-6-5-cu-ft-11-cycle-electric-dryer-white/3073087.p?skuId=3073087')


def authorization(login, password, authButton):
    while not authButton:
        try:
            time.sleep(2)
            browser.find_elements_by_xpath("//div[@class='BtnTxt']")[0].click()
            time.sleep(2)
            browser.find_elements_by_css_selector(".lam-signIn__button.btn.btn-secondary")[0].click()
            time.sleep(1)
            browser.find_elements_by_css_selector('.tb-input ')[0].send_keys(login)
            browser.find_elements_by_css_selector('.tb-input ')[1].send_keys(password)
            time.sleep(1)
            browser.find_elements_by_css_selector(
                '.btn.btn-secondary.btn-lg.btn-block.btn-leading-ficon.c-button-icon.c-button-icon-leading.cia-form__controls__submit ')[
                0].click()
            authButton = True
            return authButton
        except:
            print("login failed")


def buyer(buyButton):
    while not buyButton:
        try:
            # If this works, then the button is not pytopen
            time.sleep(3)
            addToCartBtn = addButton = browser.find_element_by_class_name("btn-disabled")

            # Button isn't open, restart the script
            print("Button isn't ready yet.")

            # Refresh page after a delay
            time.sleep(3)
            browser.refresh()

        except:

            addToCartBtn = addButton = browser.find_element_by_class_name("btn-primary")

            # Click the button
            print("Button was clicked.")
            addToCartBtn.click()
            time.sleep(4)
            goToCartBtn = addButton = browser.find_element_by_css_selector('.go-to-cart-button .btn-secondary')

            print("Go To Cart button was clicked.")
            goToCartBtn.click()

            checkoutBtn = addButton = browser.find_element_by_class_name("btn-lg")

            print("Checkout button clicked.")
            checkoutBtn.click()
            buyButton = True
            if buyButton == True:
                return buyButton


def check_out(FN=None, LN=None, adress=None, city=None, zip_code=None, phone=None):
    try:
        time.sleep(2)
        browser.find_element_by_class_name("ispu-card__switch").click()
    except:
        browser.find_elements_by_css_selector('.form-control')[0].send_keys(FN)
        browser.find_elements_by_css_selector('.form-control')[1].send_keys(LN)
        browser.find_elements_by_css_selector('.form-control')[2].send_keys(adress)
        browser.find_elements_by_css_selector('.form-control')[3].send_keys(city)
        browser.find_elements_by_css_selector('.form-control')[4].send_keys(zip_code)
        browser.find_elements_by_css_selector('.form-control')[5].send_keys(phone)
        browser.find_elements_by_css_selector('.c-dropdown')[0].selectByValue("CA")
        time.sleep(2)
        browser.find_element_by_css_selector('.go-to-cart-button .btn-secondary').click()


def main():
    buyButton = False
    authButton = False
    FN = 'Mikita'
    LN = 'Artsemyeu'
    adress = '1900 s Cirby way'
    city = 'Roseville'
    zip_code = '95661'
    phone = '2063046489'
    authorization('mikitaart2805@gmail.com', 'Barakok113', authButton)
    buyer(buyButton)
    check_out(FN, LN, adress, city, zip_code, phone)
    browser.quit()
    browser.stop()

if __name__ == '__main__':
    main()

