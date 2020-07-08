# coding=utf-8
import configparser

from snbpy.common.constant.exceptions import ConfigException, CONFIGURATION_IS_INVALID
from snbpy.common.domain.snb_config import SnbConfig


def _read_config(parser: configparser.ConfigParser) -> SnbConfig:
    try:
        config = SnbConfig()
        config.account = parser.get('ACCOUNT', 'account')
        config.key = parser.get('ACCOUNT', 'key')
        config.sign_type = parser.get('SESSION', 'sign_type')
        config.timeout = int(parser.get('SESSION', 'timeout', fallback='1000'))
        config.snb_server = parser.get('SERVER', 'snb_server')
        config.snb_port = parser.get('SERVER', 'snb_port')
        config.schema = parser.get('SERVER', 'schema', fallback='https')
        config.auto_login = bool(parser.get('SESSION', 'auto_login', fallback=False))
        return config
    except Exception:
        raise ConfigException(CONFIGURATION_IS_INVALID, "config is invalid")


def read_dictionary(dictionary: dict) -> SnbConfig:
    parser = configparser.ConfigParser()
    parser.read_dict(dictionary)
    return _read_config(parser)


def read_config(config_file_path: str) -> SnbConfig:
    """
    read config file

    [ACCOUNT]
    account=U123
    key=123

    [SESSION]
    sign_type=Default
    timeout=1000

    [SERVER]
    snb_server=localhost
    snb_port=8080

    :param config_file_path:
    :return:
    """
    parser = configparser.ConfigParser()
    parser.read(config_file_path)
    return _read_config(parser)
