from selenium.webdriver.common.by import By

class Login_User_Class:
    text_username=(By.ID,"user-name")
    text_password=(By.ID,"password")
    Clickon_Login_Xpath=(By.XPATH,"//input[@id='login-button']")
    Verify_Login_Xpath=(By.XPATH,"//div[@class='app_logo']")

    def __init__(self,driver):
        self.driver=driver

    def Enter_Username(self,name):
        self.driver.find_element(*Login_User_Class.text_username).send_keys(name)

    def Enter_Password(self,password):
        self.driver.find_element(*Login_User_Class.text_password).send_keys(password)

    def Click_On_Login(self):
        self.driver.find_element(*Login_User_Class.Clickon_Login_Xpath).click()

    def Verify_Login(self):
        Text=self.driver.find_element(*Login_User_Class.Verify_Login_Xpath).text
        if Text=='Swag Labs':
            print("Login Pass")
            return "Login Pass"

        else:
            print("Login Fail")
            return "Login Fail"