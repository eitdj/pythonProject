import configparser

config = configparser.RawConfigParser()
config.read(".\\configurations\\config.ini")


class ReadConfig:
    @staticmethod
    def getAppURL():
        config.get("login details", "URL")

    @staticmethod
    def getUsername():
        return config.get("login details", "username")

    @staticmethod
    def getPassword():
        return config.get("login details", "password")
