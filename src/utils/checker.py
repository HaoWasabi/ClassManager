from bll import *
import re

class Checker:
    @staticmethod
    def is_valid_email(email):
        email_regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
        return re.match(email_regex, email) is not None
    
    @staticmethod
    def is_valid_password(password):
        return len(password) >= 8
    
    @staticmethod
    def is_valid_repassword(password, repassword):
        return password == repassword
    
    @staticmethod
    def is_exist_email(email):
        user_bll = UserBLL()
        return user_bll.get_by_email(email) is not None