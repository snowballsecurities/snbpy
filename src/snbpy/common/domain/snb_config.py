# coding=utf-8
import logging

from snbpy.common.constant.exceptions import ConfigException, CONFIGURATION_IS_INVALID
from snbpy.common.util.string_utils import StringUtils

logger = logging.getLogger("snbpy")


class SnbConfig(object):
    """
    SDK 的 Client 的基础配置
    account     U 账户
    key	API     access Key
    sign_type	加密方式	        暂不支持
    snb_server	API 服务器地址
    snb_port	API 服务器端口
    timeout	    Http 超时时间
    cache_path	缓存路径	        暂不支持
    schema	    API Http Schema
    auto_login	是否自动登陆	    暂不支持
    """

    def __init__(self):
        self._account = None
        self._key = None
        self._sign_type = None
        self._snb_server = None
        self._snb_port = None
        self._timeout = None
        self._cache_path = None
        self._schema = None
        self._auto_login = False

    def verify(self):
        if StringUtils.is_any_blank(self.account, self.key, self.sign_type, self.snb_server, self.snb_port,
                                    self._schema):
            logger.error("configuration is invalid;; some necessary param is blank")
            raise ConfigException(CONFIGURATION_IS_INVALID, "configuration is invalid")
        if self.timeout <= 0:
            logger.error("configuration is invalid;; timeout not set or invalid")
            raise ConfigException(CONFIGURATION_IS_INVALID, "configuration is invalid")

    def __str__(self) -> str:
        return "schema: %s. server: %s, port: %s, timeout: %s" % (
            self.schema, self.snb_server, self.snb_port, self.timeout)

    @property
    def auto_login(self) -> bool:
        return self._auto_login

    @auto_login.setter
    def auto_login(self, value: bool):
        self._auto_login = value

    @property
    def schema(self):
        return self._schema

    @schema.setter
    def schema(self, schema):
        self._schema = schema

    @property
    def account(self) -> str:
        return self._account

    @account.setter
    def account(self, account):
        self._account = account

    @property
    def key(self) -> str:
        return self._key

    @key.setter
    def key(self, key):
        self._key = key

    @property
    def sign_type(self) -> str:
        return self._sign_type

    @sign_type.setter
    def sign_type(self, sign_type):
        self._sign_type = sign_type

    @property
    def snb_server(self) -> str:
        return self._snb_server

    @snb_server.setter
    def snb_server(self, snb_server):
        self._snb_server = snb_server

    @property
    def snb_port(self) -> str:
        return self._snb_port

    @snb_port.setter
    def snb_port(self, snb_port):
        self._snb_port = snb_port

    @property
    def timeout(self) -> int:
        return self._timeout

    @timeout.setter
    def timeout(self, timeout):
        self._timeout = timeout

    @property
    def cache_path(self) -> str:
        return self._cache_path

    @cache_path.setter
    def cache_path(self, cache_path: str):
        self._cache_path = cache_path
