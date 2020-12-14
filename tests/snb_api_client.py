import logging
import time
from unittest import TestCase

from snbpy.common.constant.exceptions import InvalidParamException, INVALID_ORDER_ID
from snbpy.common.constant.snb_constant import SecurityType, OrderSide, Currency, OrderType, TimeInForce
from snbpy.common.domain.snb_config import SnbConfig
from snbpy.snb_api_client import SnbHttpClient

logging.basicConfig(level=logging.DEBUG)
class TestArrayUtils(TestCase):
    def setUp(self) -> None:
        self.config = SnbConfig()
        # 替换掉这里
        self.config.account = "1234567"
        # 替换掉这里
        self.config.key = 'abcdefg'
        self.config.sign_type = 'None'
        self.config.snb_server = 'sandbox.snbsecurities.com'
        self.config.snb_port = '443'
        self.config.timeout = 1000
        self.config.schema = 'https'
        self.client = SnbHttpClient(self.config)

    def test_login(self):
        self.client.login()
        self.assertIsNotNone(self.client.token)
        self.assertGreater(self.client.token_expire_time, 0)

    def test_get_order_list(self):
        self.client.login()
        order_list_response = self.client.get_order_list()
        self.assertIsNotNone(order_list_response)
        self.assertTrue(order_list_response.succeed())

    def test_get_positions(self):
        self.client.login()
        position_list = self.client.get_position_list()
        self.assertIsNotNone(position_list)
        self.assertTrue(position_list.succeed())

    def test_get_balance(self):
        self.client.login()
        balance = self.client.get_balance()
        self.assertIsNotNone(balance)
        self.assertTrue(balance.succeed())

    def test_get_security_detail(self):
        self.client.login()
        security_detail = self.client.get_security_detail("00700")
        self.assertIsNotNone(security_detail)
        self.assertTrue(security_detail.succeed())

    def test_get_order_by_id(self):
        self.client.login()
        order = self.client.get_order_by_id("1592188441")
        self.assertIsNotNone(order)
        self.assertTrue(order.succeed())

    def test_cancel_order(self):
        self.client.login()
        order_id = str(int(time.time()))
        place_order = self.client.place_order(order_id, SecurityType.STK, "00700", "", OrderSide.BUY, Currency.HKD,
                                              100, 100.1, OrderType.LIMIT, TimeInForce.DAY, True)
        self.assertIsNotNone(place_order)
        self.assertTrue(place_order.succeed())

        cancel_order = self.client.cancel_order(str(int(time.time())), order_id)
        self.assertIsNotNone(cancel_order)
        self.assertTrue(cancel_order.succeed())

    def test_place_order(self):
        self.client.login()
        order_id = str(int(time.time()))
        place_order = self.client.place_order(order_id, SecurityType.STK, "00700", "", OrderSide.BUY, Currency.HKD,
                                              100, 100.1, OrderType.LIMIT, TimeInForce.DAY, True)
        self.assertIsNotNone(place_order)
        self.assertTrue(place_order.succeed())

    def test_invalid_order_id(self):
        self.client.login()
        with self.assertRaises(InvalidParamException) as context:
            self.client.place_order("", SecurityType.STK, "00700", "HKEX", OrderSide.BUY, Currency.HKD,
                                                  100, 100.1, OrderType.LIMIT, TimeInForce.DAY, True)
            self.assertTrue(hasattr(context.exception, "code"))
            self.assertTrue(INVALID_ORDER_ID in context.exception.code)

    def test_get_token_status(self):
        self.client.login()
        token = self.client.get_token_status()
        self.assertIsNotNone(token)
        self.assertTrue(token.succeed())

    def test_get_transaction_list(self):
        self.client.login()
        transaction_list = self.client.get_transaction_list()
        self.assertIsNotNone(transaction_list)
        self.assertTrue(transaction_list.succeed())
