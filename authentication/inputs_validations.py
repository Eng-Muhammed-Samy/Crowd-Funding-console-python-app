import re


class Validation:

    @staticmethod
    def validate_f_name(f_name):
        if len(f_name) >= 4 and f_name.isalpha():
            return True
        return False

    @staticmethod
    def validate_l_name(l_name):
        if len(l_name) >= 4 and l_name.isalpha():
            return True
        return False

    @staticmethod
    def validate_email(email):
        regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
        if re.fullmatch(regex, email):
            return True
        return False

    @staticmethod
    def validate_password(password, confirm_password):
        if len(password) >= 5 and password == confirm_password:
            return True
        return False
