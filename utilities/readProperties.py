import configparser

config = configparser.RawConfigParser()
config.read(".\\Configurations\\config.ini")


class ReadConfig():
    @staticmethod
    def ApplicationURL():
        url = config.get('common info', 'baseURL')
        return url

    @staticmethod
    def Username():
        UserName = config.get('common info', 'username')
        return UserName

    @staticmethod
    def Password():
        PassWord = config.get('common info', 'password')
        return PassWord

    @staticmethod
    def Firstname():
        FName = config.get('common info', 'Fname')
        return FName

    @staticmethod
    def Lastname():
        LName = config.get('common info', 'Lname')
        return LName

    @staticmethod
    def Pcode():
        pinCode = config.get('common info', 'Pincode')
        return pinCode