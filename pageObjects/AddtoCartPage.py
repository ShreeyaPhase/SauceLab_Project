from selenium import webdriver
from selenium.webdriver.common.by import By

class Add_To_Cart_Class:
    Add_Back_pack_ID=(By.ID,"add-to-cart-sauce-labs-backpack")
    Add_Fleece_Jacket_ID=(By.ID,"add-to-cart-sauce-labs-fleece-jacket")
    Add_Bike_light_ID=(By.ID,"add-to-cart-sauce-labs-bike-light")
    Click_on_cart_Xpath=(By.XPATH,"//a[@class='shopping_cart_link']")
    Clik_on_Continue_shopping_Id=(By.ID,"continue-shopping")
    Clik_Checkout_xpath=(By.XPATH,"//button[@id='checkout']")
    Verify_On_checkoutpage=(By.XPATH,"//span[contains(.,'Checkout: Your Information')]")
    Enter_firstname_on_chekout_xpath=(By.XPATH,"//input[@placeholder='First Name']")
    Enter_Lastname_on_checkout_xpath=(By.XPATH,"//input[@id='last-name']")
    Enter_pincode_on_checkout_xpath=(By.XPATH,"//input[@placeholder='Zip/Postal Code']")
    Click_on_continue_xpath=(By.XPATH,"//input[@id='continue']")
    Verify_on_finishPagexpath=(By.XPATH,"//span[contains(.,'Checkout: Overview')]")
    Click_on_finish_button_xpath=(By.XPATH,"//button[@id='finish']")

    def __init__(self,driver):
        self.driver=driver
    def Add_back_pack_to_cart(self):
        self.driver.find_element(*Add_To_Cart_Class.Add_Back_pack_ID).click()
    def Add_fleece_jacket_to_cart(self):
        self.driver.find_element(*Add_To_Cart_Class.Add_Fleece_Jacket_ID).click()
    def Add_to_cart_bike_light(self):
        self.driver.find_element(*Add_To_Cart_Class.Add_Bike_light_ID).click()
    def Click_on_Cart(self):
        self.driver.find_element(*Add_To_Cart_Class.Click_on_cart_Xpath).click()

    def Verify_You_Are_On_ChekoutPage(self):
       Text= self.driver.find_element(*Add_To_Cart_Class.Verify_On_checkoutpage).text
       if Text=="Your Cart":
           print("Right Page")
           #self.driver.save_screenshot("C:\Users\dound\PycharmProjects\SauceLab_Project\screenshots\\Right.png")
           return "Right Page"
       else:
           print("Wrong page")
           return "Wrong page"

       