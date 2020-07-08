# coding=utf-8
from enum import Enum, unique

API_VERSION = '1.0.0-SNAPSHOT'


@unique
class Currency(Enum):
    ALL = 'ALL'
    USX = 'USX'
    CNY = 'CNY'
    USD = 'USD'
    SEK = 'SEK'
    SGD = 'SGD'
    TRY = 'TRY'
    ZAR = 'ZAR'
    JPY = 'JPY'
    AUD = 'AUD'
    CAD = 'CAD'
    CHF = 'CHF'
    CNH = 'CNH'
    HKD = 'HKD'
    NZD = 'NZD'
    CZK = 'CZK'
    DKK = 'DKK'
    HUF = 'HUF'
    NOK = 'NOK'
    PLN = 'PLN'
    EUR = 'EUR'
    GBP = 'GBP'
    ILS = 'ILS'
    MXN = 'MXN'
    RUB = 'RUB'
    KRW = 'KRW'


@unique
class OrderType(Enum):
    LIMIT = 'LIMIT'
    MARKET = 'MARKET'
    AT = 'AT'
    ATL = 'ATL'
    SSL = 'SSL'
    SEL = 'SEL'
    STOP = 'STOP'
    STOP_LIMIT = 'STOP_LIMIT'
    TRAIL = 'TRAIL'
    TRAIL_LIMIT = 'TRAIL_LIMIT'
    LIMIT_ON_OPENING = 'LIMIT_ON_OPENING'
    MARKET_ON_OPENING = 'MARKET_ON_OPENING'
    LIMIT_ON_CLOSE = 'LIMIT_ON_CLOSE'
    MARKET_ON_CLOSE = 'MARKET_ON_CLOSE'


@unique
class SecurityType(Enum):
    ALL = 'ALL'
    STK = 'STK'
    FUT = 'FUT'
    OPT = 'OPT'
    FOP = 'FOP'
    WAR = 'WAR'
    MLEG = 'MLEG'
    CASH = 'CASH'
    CFD = 'CFD'
    CMDTY = 'CMDTY'
    FUND = 'FUND'
    IOPT = 'IOPT'
    BOND = 'BOND'


@unique
class OrderSide(Enum):
    BUY = 'BUY'
    SELL = 'SELL'


@unique
class OrderStatus(Enum):
    INVALID = 'INVALID'
    EXPIRED = 'EXPIRED'
    NO_REPORT = 'NO_REPORT'
    WAIT_REPORT = 'WAIT_REPORT'
    REPORTED = 'REPORTED'
    PART_CONCLUDED = 'PART_CONCLUDED'
    CONCLUDED = 'CONCLUDED'
    WITHDRAWING = 'WITHDRAWING'
    WAIT_WITHDRAW = 'WAIT_WITHDRAW'
    PART_WAIT_WITHDRAW = 'PART_WAIT_WITHDRAW'
    PART_WITHDRAW = 'PART_WITHDRAW'
    WITHDRAWED = 'WITHDRAWED'
    REPLACING = 'REPLACING'
    WAIT_REPLACE = 'WAIT_REPLACE'
    REPLACED = 'REPLACED'


@unique
class HttpMethod(Enum):
    GET = 'GET'
    POST = 'POST'
    DELETE = 'DELETE'


@unique
class TimeInForce(Enum):
    DAY = 'DAY'
    GTC = 'GTC'
