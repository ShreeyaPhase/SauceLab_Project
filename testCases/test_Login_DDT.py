import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from pageObjects.LoginPageObject import Login_User_Class
from utilities import ExcelFileOperation
from utilities import Readconfig

class Test_Login_DDT:
    LoginUrl=Readconfig.getURL()
    UserName=Readconfig.getUserName()
    Password=Readconfig.getPassword()
    path="C:\\Users\\dound\\PycharmProjects\\SauceLab_Project\\testCases\testData\\Login_Data.xlsx"

    def test_login_ddt_001(self,setup):
        self.driver=setup
        self.lp=Login_User_Class(self.driver)
        self.rows=ExcelFileOperation.rows_count(self.path,'Sheet1')
        print(self.rows)
        Result_List=[]
        for r in range(2,self.rows+1):
            self.userName=ExcelFileOperation.ReadData(self.path,'Sheet1',r,1)
            self.password=ExcelFileOperation.ReadData(self.path,'Sheet1',r,2)
            self.Exp_Result=ExcelFileOperation.ReadData(self.path,'Sheet1',r,3)
            self.driver.get(self.LoginUrl)
            self.lp.Enter_Username(self.UserName)
            print("UserName-->"+self.UserName)
            self.lp.Enter_Password(self.password)
            print("Password-->"+self.password)
            self.lp.Click_On_Login()
            if self.lp.Verify_Login()=="Login Pass":
                if self.Exp_Result=='Pass':
                    Result_List.append("Pass")
                    ExcelFileOperation.WriteData(self.path,'Sheet1',4,"Pass")
                    self.driver.save_screenshot("C:\\Users\\dound\\PycharmProjects\\SauceLab_Project\\screenshots\\Login_Pass.png")
                    self.driver.find_element(By.XPATH,"//button[normalize-space()='Open Menu'])[1]").click()
                    self.driver.find_element(By.XPATH,"(//a[normalize-space()='Logout'])[1]").click()
                    #assert True

                elif self.Exp_Result=="Fail":
                   Result_List.append("Fail")
                   ExcelFileOperation.WriteData(self.path,'Sheet1',r,4,"Pass")
                   self.driver.save_screenshot("C:\\Users\\dound\\PycharmProjects\\SauceLab_Project\\screenshots\\Login_Pass.png")
                   self.driver.find_element(By.XPATH, "//button[normalize-space()='Open Menu'])[1]").click()
                   self.driver.find_element(By.XPATH, "(//a[normalize-space()='Logout'])[1]").click()
            else: #login fail
                if self.Exp_Result=='Pass':
                    Result_List.append("Fail")
                    ExcelFileOperation.WriteData(self.path,'Sheet1',r,4,'Fail')
                    self.driver.save_screenshot("C:\\Users\\dound\\PycharmProjects\\SauceLab_Project\\screenshots\\Login_Pass.png")
                elif self.Exp_Result=="Fail":
                    Result_List.append("Pass")
                    ExcelFileOperation.WriteData(self.path,'Sheet1',r,4,"Fail")
                    self.driver.save_screenshot(
                        "C:\\Users\\dound\\PycharmProjects\\SauceLab_Project\\screenshots\\Login_Pass.png")
                self.driver.save_screenshot(
                    "C:\\Users\\dound\\PycharmProjects\\SauceLab_Project\\screenshots\\Login_Fail.png")
            print(Result_List)
            if "Fail" in Result_List:
                assert False
            else:
                assert True





