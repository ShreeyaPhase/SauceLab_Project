import configparser

config=configparser.RawConfigParser()
config.read("C:\\Users\\dound\\PycharmProjects\\SauceLab_Project\\configurations\\config.ini")

class Readconfig:
    @staticmethod
    def getURL():
        LoginUrl=config.get('user info','loginUrl')
        return LoginUrl
    @staticmethod
    def getUserName():
        UserName=config.get('user info','User_name')
        return UserName
    @staticmethod
    def getPassword():
        Password=config.get('user info','Password')
        return Password


