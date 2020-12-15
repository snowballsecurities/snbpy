# coding=utf-8
import abc
import json
import logging
import time

import requests

from snbpy.common.constant.exceptions import ApiExecuteException, API_EXCEPTION, TokenInvalid, LOGIN_NEEDED
from snbpy.common.constant.snb_constant import API_VERSION, HttpMethod, SecurityType, OrderSide, Currency, TimeInForce, \
    OrderType
from snbpy.common.domain.request import HttpRequest, AccessTokenRequest, GetOrderListRequest, GetPositionListRequest, \
    GetBalanceRequest, GetSecurityDetailRequest, GetOrderByOrderIdRequest, CancelOrderRequest, PlaceOrderRequest, \
    GetTokenStatusRequest, GetTransactionListRequest
from snbpy.common.domain.response import HttpResponse
from snbpy.common.domain.snb_config import SnbConfig
from snbpy.common.util.string_utils import StringUtils

logger = logging.getLogger("snbpy")


class SnbApiClient(metaclass=abc.ABCMeta):
    """
    API Client 框架
    """

    def __init__(self, config: SnbConfig, token: str = None, token_expire_time: int = 0):
        logger.debug("init snb api client;; config: %s", config)
        config.verify()
        logger.debug("config is legal")
        self._config = config
        self._token = token
        self._token_expire_time = token_expire_time
        self._headers = {"User-Agent": "snbpy/%s" % API_VERSION,
                         "Accecpt": "Accept:application/vnd.snowx+json; version=1.0",
                         "Cache-Control": "no-cache",
                         "Connection": "Keep-Alive"}

    @property
    def token(self):
        return self._token

    @token.setter
    def token(self, token):
        self._token = token

    @property
    def token_expire_time(self):
        return self._token_expire_time

    @token_expire_time.setter
    def token_expire_time(self, token_expire_time):
        self._token_expire_time = token_expire_time

    @abc.abstractmethod
    def _parse_response(self, response_str: str) -> HttpResponse:
        """
        解析请求返回值
        :param response_str: response body
        :return: HttpResponse
        """
        pass

    @abc.abstractmethod
    def _do_execute(self, url: str, params: dict, header: dict, timeout: int, method: HttpMethod) -> str:
        """
        执行请求
        :param url:
        :param params:
        :param header:
        :param timeout:
        :param method:
        :return: response body
        """
        pass

    @abc.abstractmethod
    def _prepare_param(self, request: HttpRequest) -> dict:
        """
        准备请求参数
        :param request: 请求对象
        :return: dict
        """
        pass

    def execute(self, request: HttpRequest) -> HttpResponse:
        logger.debug("execute request;; request: %s; method: %s ;url: %s", request.__class__, request.method,
                     request.url)
        logger.debug("verify request;; request: %s; method: %s ;url: %s", request.__class__, request.method,
                     request.url)
        request.verify()
        logger.debug("request verify passed;; request: %s; method: %s ;url: %s", request.__class__, request.method,
                     request.url)
        headers = self._headers
        logger.debug("send http request: %s", request)
        if request.auth() > 0 and (StringUtils.is_blank(self._token) or self._token_expire_time < time.time()):
            raise TokenInvalid(LOGIN_NEEDED, "login first")
        if request.auth() > 0:
            headers['Cookie'] = 'access_token=%s' % self._token
        try:
            response_str = self._do_execute(request.url, self._prepare_param(request), headers, self._config.timeout,
                                            request.method)
        except Exception as e:
            logger.error("http excepiton;; %s", e)
            raise ApiExecuteException(API_EXCEPTION, "http exception" + str(e))
        return self._parse_response(response_str)


class TradeInterface(object):
    @abc.abstractmethod
    def login(self):
        """ 登陆接口
        需要在 client 的 config 对象中设置好用户名和秘钥
        :return:
        {
            "result_code": "60000",
            "msg": null,
            "result_data": {
                "access_token": "9fk3HoyaD2EgxAC1sPg1dP2QjOwJDPSn",
                "expiry_time": 1591696693584
            }
        }
        """

    @abc.abstractmethod
    def get_token_status(self) -> HttpResponse:
        """ 查询 token 状态

        :return: HttpResponse
        {
            "result_code": "60000",
            "msg": null,
            "result_data": {
                "access_token": "9fk3HoyaD2EgxAC1sPg1dP2QjOwJDPSn",
                "expiry_time": 1591696693584
            }
        }
        """
        pass

    @abc.abstractmethod
    def get_order_list(self, page: int = 1, size: int = 10, status: str = None,
                       security_type: str = "STK,OPT,WAR,IOPT,FUT") -> HttpResponse:
        pass

    @abc.abstractmethod
    def get_position_list(self, security_type: str = "STK,OPT,WAR,IOPT,FUT") -> HttpResponse:
        pass

    @abc.abstractmethod
    def get_balance(self) -> HttpResponse:
        pass

    @abc.abstractmethod
    def get_security_detail(self, symbol: str):
        pass

    @abc.abstractmethod
    def get_order_by_id(self, order_id: str):
        pass

    @abc.abstractmethod
    def place_order(self, order_id: str, security_type: SecurityType, symbol: str, exchange: str,
                    side: OrderSide, currency: Currency, quantity: int, price: float = 0,
                    order_type: OrderType = OrderType.LIMIT, tif: TimeInForce = TimeInForce.DAY,
                    force_only_rth: bool = True):
        """下单
        :param order_id: 订单 ID
        :param security_type: 证券类型，参见数据字典：SecurityType
        :param symbol: 证券代码
        :param exchange: 交易所代码
        :param side: 交易方向，参见：数据字典OrderSide
        :param currency: 币种，参见：数据字典Currency
        :param quantity: 交易数量 ，最小为1
        :param price: 限价下单必传，市价下单传任何均为0
        :param order_type: 订单类型，参见：数据字典OrderType
        :param tif: 订单有效期，参见：数据字典TimeInForce
        :param force_only_rth: 是否仅限盘中交易
        :return:
        {
            "result_code": "60000",
            "msg": null,
            "result_data": {
                "memo": "",
                "id": "sdk000000021",
                "status": "REPORTED"
            }
        }
        """
        pass

    @abc.abstractmethod
    def cancel_order(self, order_id: str, origin_order_id: str) -> HttpResponse:
        """
        撤单
        :param order_id: 撤单请求 ID
        :param origin_order_id: 被撤订单 ID
        :return:
        """
        pass

    @abc.abstractmethod
    def get_transaction_list(self, page=1, size=10, side=None, order_time_min=None, order_time_max=None):
        pass


class SnbHttpClient(SnbApiClient, TradeInterface):
    def __init__(self, config: SnbConfig):
        self.session = requests.session()
        super().__init__(config)

    def _parse_response(self, response_str: str) -> HttpResponse:
        dic = json.loads(response_str)
        # todo 自动踢出
        if 'result_code' not in dic \
                or 'msg' not in dic \
                or 'result_data' not in dic:
            raise ApiExecuteException(API_EXCEPTION, 'response result invalid')
        response = HttpResponse()
        response.data = dic.get('result_data')
        response.result_code = dic.get('result_code')
        response.message = StringUtils.default_string(dic.get('msg'))
        response.result_str = response_str
        return response

    def _do_execute(self, url: str, params: dict, header: dict, timeout: int, method: HttpMethod) -> str:
        request_path = "%s://%s:%s/%s" % (self._config.schema, self._config.snb_server, self._config.snb_port, url)
        logger.debug("do execute;; url: %s, params: %s, header: %s, timeout: %s, method: %s", url, params, header,
                     timeout, method)

        try:
            if method == HttpMethod.GET:
                return self.session.get(url=request_path, headers=header, params=params, timeout=timeout).content.decode(
                    "utf-8")
            elif method == HttpMethod.POST:
                return self.session.post(url=request_path, headers=header, data=params, timeout=timeout).content.decode(
                    "utf-8")
            elif method == HttpMethod.DELETE:
                return self.session.delete(url=request_path, headers=header, params=params, timeout=timeout).content.decode(
                    "utf-8")

        except Exception as e:
            logger.error("do execute with exception;; %s", e)
            raise e

    def _prepare_param(self, request: HttpRequest) -> dict:
        return request.generate_params()

    def login(self) -> HttpResponse:
        login_request = AccessTokenRequest(self._config.account, self._config.key)
        logger.debug("login request: %s", login_request)
        response = self.execute(login_request)
        logger.debug("login result: %s", response)
        if not response.succeed():
            logger.warning("login failed %s", response)
            raise ApiExecuteException(API_EXCEPTION, "login failed")
        self._token = response.data.get('access_token')
        self._token_expire_time = response.data.get('expiry_time')
        return response

    def get_token_status(self) -> HttpResponse:
        token_request = GetTokenStatusRequest(self._config.account, self._token)
        response = self.execute(token_request)
        return response

    def get_order_list(self, page: int = 1, size: int = 10, status: str = None,
                       security_type: str = "STK,OPT,WAR,IOPT,FUT") -> HttpResponse:
        order_list_request = GetOrderListRequest(self._config.account, page, size, status, security_type)
        response = self.execute(order_list_request)
        return response

    def get_position_list(self, security_type: str = "STK,OPT,WAR,IOPT,FUT") -> HttpResponse:
        position_list_request = GetPositionListRequest(self._config.account, security_type)
        response = self.execute(position_list_request)
        return response

    def get_balance(self) -> HttpResponse:
        balance_request = GetBalanceRequest(self._config.account)
        response = self.execute(balance_request)
        return response

    def get_security_detail(self, symbol: str):
        security_detail_request = GetSecurityDetailRequest(self._config.account, symbol)
        response = self.execute(security_detail_request)
        return response

    def get_order_by_id(self, order_id: str):
        order_request = GetOrderByOrderIdRequest(account_id=self._config.account, order_id=order_id)
        response = self.execute(order_request)
        return response

    def place_order(self, order_id: str, security_type: SecurityType, symbol: str, exchange: str,
                    side: OrderSide, currency: Currency, quantity: int, price: float = 0,
                    order_type: OrderType = OrderType.LIMIT, tif: TimeInForce = TimeInForce.DAY,
                    force_only_rth: bool = True):
        place_order_request = PlaceOrderRequest(self._config.account, order_id, security_type, symbol, exchange,
                                                side, currency, quantity, price, order_type, tif, force_only_rth)
        response = self.execute(place_order_request)
        return response

    def cancel_order(self, order_id: str, origin_order_id: str):
        cancel_order_request = CancelOrderRequest(account_id=self._config.account, origin_order_id=origin_order_id,
                                                  order_id=order_id)
        response = self.execute(cancel_order_request)
        return response

    def get_transaction_list(self, page=1, size=10, side=None, order_time_min=None, order_time_max=None):
        transaction_request = GetTransactionListRequest(self._config.account, page, size, side, order_time_min,
                                                        order_time_max)
        response = self.execute(transaction_request)
        return response
