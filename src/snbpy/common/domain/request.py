import abc
import logging

from snbpy.common.constant.exceptions import InvalidParamException, INVALID_ORDER_ID
from snbpy.common.constant.snb_constant import HttpMethod, OrderSide, SecurityType, OrderType, Currency, TimeInForce, OrderIdType
from snbpy.common.util.string_utils import StringUtils

logger = logging.getLogger("snbpy")

class HttpRequest(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def auth(self) -> int:
        pass

    @abc.abstractmethod
    def verify(self) -> bool:
        pass

    @property
    @abc.abstractmethod
    def method(self) -> HttpMethod:
        pass

    @property
    @abc.abstractmethod
    def url(self) -> str:
        pass

    @abc.abstractmethod
    def generate_params(self) -> dict:
        pass


class AccessTokenRequest(HttpRequest):
    def __init__(self, account_id: str, secret_key: str):
        self._account_id = account_id
        self._secret_key = secret_key

    @property
    def account_id(self) -> str:
        return self._account_id

    @account_id.setter
    def account_id(self, account_id: str):
        self._account_id = account_id

    @property
    def secret_key(self) -> str:
        return self._secret_key

    @secret_key.setter
    def secret_key(self, secret_key: str):
        self._secret_key = secret_key

    @property
    def url(self) -> str:
        return "auth/%s/access-token" % self._account_id

    def auth(self) -> int:
        return 0

    @property
    def method(self) -> HttpMethod:
        return HttpMethod.POST

    def verify(self) -> bool:
        return StringUtils.is_none_blank(self._account_id, self._secret_key)

    def generate_params(self) -> dict:
        return {"secret_key": self._secret_key}


class GetOrderListRequest(HttpRequest):

    def __init__(self, account_id: str, page: int = 1, size: int = 20, status: str = None,
                 security_type: str = "STK,OPT,WAR,IOPT,FUT"):
        self._account_id = account_id
        self._page = page
        self._size = size
        self._status = status
        self._security_type = security_type

    @property
    def page(self):
        return self._page

    @page.setter
    def page(self, value):
        self._page = value

    @property
    def size(self):
        return

    @size.setter
    def size(self, size):
        self._size = size

    @property
    def status(self):
        return

    @property
    def security_type(self):
        return

    @security_type.setter
    def security_type(self, security_type):
        self._security_type = security_type

    @status.setter
    def status(self, status):
        self._status = status

    @property
    def account_id(self) -> str:
        return self._account_id

    @account_id.setter
    def account_id(self, value: str):
        self._account_id = value

    def auth(self) -> int:
        return 1

    def verify(self) -> bool:
        return StringUtils.is_not_blank(self._account_id)

    @property
    def method(self) -> HttpMethod:
        return HttpMethod.GET

    @property
    def url(self) -> str:
        return "order"

    def generate_params(self) -> dict:
        return {"account_id": self._account_id,
                "page": self._page,
                "size": self._size,
                "status": self._status,
                "security_type": self._security_type}


class PlaceOrderRequest(HttpRequest):

    def __init__(self, account_id: str, order_id: str, security_type: SecurityType, symbol: str, exchange: str,
                 side: OrderSide, currency: Currency, quantity: int, price: float = 0,
                 order_type: OrderType = OrderType.LIMIT, tif: TimeInForce = TimeInForce.DAY,
                 force_only_rth: bool = True, stop_price: float = 0, parent: str = None, order_id_type: OrderIdType = OrderIdType.CLIENT):
        self._account_id = account_id
        self._order_id = order_id
        self._security_type = security_type
        self._symbol = symbol
        self._exchange = exchange
        self._order_type = order_type
        self._side = side
        self._currency = currency
        self._quantity = quantity
        self._price = price
        self._tif = tif
        self._force_only_rth = force_only_rth
        self._stop_price = stop_price
        self._parent = parent
        self._order_id_type = order_id_type

    def auth(self) -> int:
        return 1

    def verify(self) -> bool:
        if StringUtils.is_blank(self._order_id):
            logger.error("order id cannot by blank;; order_id: %s", self._order_id)
            raise InvalidParamException(INVALID_ORDER_ID, "INVALID ORDER ID")
        return StringUtils.is_none_blank(self._account_id, self._order_id)

    @property
    def method(self) -> HttpMethod:
        return HttpMethod.POST

    @property
    def url(self) -> str:
        return "order/%s" % (self._order_id)

    def generate_params(self) -> dict:
        return {"security_type": self._security_type.value,
                "account_id": self._account_id,
                "symbol": self._symbol,
                "exchange": self._exchange,
                "order_type": self._order_type.value,
                "side": self._side.value,
                "currency": self._currency.value,
                "quantity": self._quantity,
                "price": self._price,
                "tif": self._tif.value,
                "rth": self._force_only_rth,
                "stop_price": self._stop_price,
                "parent": self._parent,
                "order_id_type": self._order_id_type.value
                }


class CancelOrderRequest(HttpRequest):
    def __init__(self, account_id: str, order_id: str, origin_order_id: str, order_id_type: OrderIdType = OrderIdType.CLIENT):
        self._origin_order_id = origin_order_id
        self._order_id = order_id
        self._account_id = account_id
        self._order_id_type = order_id_type

    @property
    def account_id(self) -> str:
        return self._account_id

    @account_id.setter
    def account_id(self, value: str):
        self._account_id = value

    @property
    def order_id(self) -> str:
        return self._order_id

    @order_id.setter
    def order_id(self, value: str):
        self._order_id = value

    @property
    def origin_order_id(self) -> str:
        return self._origin_order_id

    @origin_order_id.setter
    def origin_order_id(self, value: str):
        self._origin_order_id = value

    def auth(self) -> int:
        return 1

    def verify(self) -> bool:
        return StringUtils.is_none_blank(self._order_id, self._origin_order_id, self._account_id)

    @property
    def method(self) -> HttpMethod:
        return HttpMethod.DELETE

    @property
    def url(self) -> str:
        return "order/%s" % self._origin_order_id

    def generate_params(self) -> dict:
        return {"new_id": self._order_id, "account_id": self._account_id, "order_id_type": self._order_id_type.value}


class GetOrderByOrderIdRequest(HttpRequest):
    def __init__(self, account_id: str, order_id: str):
        self._account_id = account_id
        self._order_id = order_id

    @property
    def order_id(self) -> str:
        return self._order_id

    @order_id.setter
    def order_id(self, value: str):
        self._order_id = value

    @property
    def account_id(self) -> str:
        return self._account_id

    @account_id.setter
    def account_id(self, value: str):
        self._account_id = value

    def auth(self) -> int:
        return 1

    def verify(self) -> bool:
        return True

    @property
    def method(self) -> HttpMethod:
        return HttpMethod.GET

    @property
    def url(self) -> str:
        return "order/%s" % self._order_id

    def generate_params(self) -> dict:
        return {"account_id": self._account_id}


class GetTransactionListRequest(HttpRequest):
    def __init__(self, account_id, page=1, size=20, side=None, order_time_min=None, order_time_max=None):
        self._account_id = account_id
        self._page = page
        self._size = size
        self._side = side
        self._order_time_min = order_time_min
        self._order_time_max = order_time_max

    @property
    def account_id(self):
        return self._account_id

    @account_id.setter
    def account_id(self, account_id):
        self._account_id = account_id

    @property
    def page(self):
        return self._page

    @page.setter
    def page(self, page):
        self._page = page

    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, size):
        self._size = size

    @property
    def side(self):
        return self._side

    @side.setter
    def side(self, side):
        self._side = side

    @property
    def order_time_min(self):
        return self._order_time_min

    @order_time_min.setter
    def order_time_min(self, order_time_min):
        self._order_time_min = order_time_min

    @property
    def order_time_max(self):
        return self._order_time_max

    @order_time_max.setter
    def order_time_max(self, order_time_max):
        self._order_time_max = order_time_max

    def auth(self) -> int:
        return 1

    def verify(self) -> bool:
        return StringUtils.is_none_blank(self._account_id)

    @property
    def method(self) -> HttpMethod:
        return HttpMethod.GET

    @property
    def url(self) -> str:
        return "trade"

    def generate_params(self) -> dict:
        return {"account_id": self._account_id,
                "page": self._page,
                "size": self._size,
                "side": self._side,
                "order_time_min": self._order_time_min,
                "order_time_max": self._order_time_max}


class GetPositionListRequest(HttpRequest):
    def __init__(self, account_id: str, security_type: str = "STK,OPT,WAR,IOPT,FUT"):
        self._account_id = account_id
        self._security_type = security_type

    @property
    def account_id(self) -> str:
        return self._account_id

    @account_id.setter
    def account_id(self, value: str):
        self._account_id = value

    def auth(self) -> int:
        return 1

    def verify(self) -> bool:
        return True

    @property
    def method(self) -> HttpMethod:
        return HttpMethod.GET

    @property
    def url(self) -> str:
        return "position"

    def generate_params(self) -> dict:
        return {"account_id": self._account_id, "security_type": self._security_type}


class GetBalanceRequest(HttpRequest):

    def __init__(self, account_id: str):
        self._account_id = account_id

    @property
    def account_id(self) -> str:
        return self._account_id

    @account_id.setter
    def account_id(self, value: str):
        self._account_id = value

    def auth(self) -> int:
        return 1

    def verify(self) -> bool:
        return StringUtils.is_not_blank(self._account_id)

    @property
    def method(self) -> HttpMethod:
        return HttpMethod.GET

    @property
    def url(self) -> str:
        return "funds"

    def generate_params(self) -> dict:
        return {"account_id": self._account_id}


class GetTokenStatusRequest(HttpRequest):

    def __init__(self, account_id: str, token: str):
        self._account_id = account_id
        self._token = token

    @property
    def account_id(self):
        return self._account_id

    @account_id.setter
    def account_id(self, account_id):
        self._account_id = account_id

    @property
    def token(self):
        return self._token

    @token.setter
    def token(self, token):
        self._token = token

    def auth(self) -> int:
        return 1

    def verify(self) -> bool:
        return True

    @property
    def method(self) -> HttpMethod:
        return HttpMethod.GET

    @property
    def url(self) -> str:
        return "/auth/%s/access-token/%s" % (self._account_id, self._token)

    def generate_params(self) -> dict:
        return {}


class GetSecurityDetailRequest(HttpRequest):
    def __init__(self, account_id: str, symbol: str):
        self._symbol = symbol
        self._account_id = account_id

    @property
    def symbol(self) -> str:
        return self._symbol

    @symbol.setter
    def symbol(self, value: str):
        self._symbol = value

    def auth(self) -> int:
        return 1

    def verify(self) -> bool:
        return StringUtils.is_not_blank(self._symbol)

    @property
    def method(self) -> HttpMethod:
        return HttpMethod.GET

    @property
    def url(self) -> str:
        return "security/details"

    def generate_params(self) -> dict:
        return {"symbol": self._symbol, "account_id": self._account_id}
