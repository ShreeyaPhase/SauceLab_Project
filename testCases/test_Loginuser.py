from selenium import webdriver
from selenium.webdriver.common.by import By
from pageObjects.LoginPageObject import Login_User_Class

class Test_UserProfile():
    def test_Login001(self,setup):
        self.driver=setup
        self.ur=Login_User_Class(self.driver)
        self.driver.get("https://www.saucedemo.com/")
        self.ur.Enter_Username("standard_user")
        self.ur.Enter_Password("secret_sauce")
        self.ur.Click_On_Login()

        if self.ur.Verify_Login()=="Login Pass":
            self.driver.save_screenshot("C:\\Users\\dound\\PycharmProjects\\SauceLab_Project\\screenshots\\login_pass.png")
            self.driver.close()
            assert True

        else:
            self.driver.save_screenshot("C:\\Users\\dound\\PycharmProjects\\SauceLab_Project\\screenshots\\login_fail.png")
            assert False