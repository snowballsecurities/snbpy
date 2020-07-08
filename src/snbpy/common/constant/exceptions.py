# coding=utf-8
CONFIGURATION_IS_INVALID = '001001'

API_EXCEPTION = '002001'
TOKEN_INVALID = '002002'
LOGIN_NEEDED = '002003'
KEY_INVALID = '002004'


class SnbException(Exception):
    def __init__(self, code, msg):
        self.code = code
        self.msg = msg


class ConfigException(SnbException):
    pass


class ApiExecuteException(SnbException):
    pass


class TokenInvalid(SnbException):
    pass
