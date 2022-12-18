import configparser

config = configparser.RawConfigParser()
config.read(".\\Configuration\\config.ini")


class readConfig:
    @staticmethod
    def getApplicationURL():
        url = config.get("common data", "baseURL")
        return url

    @staticmethod
    def getUsername():
        username = config.get('common data', 'username')
        return username

    @staticmethod
    def getPassword():
        password = config.get('common data', 'password')
        return password
