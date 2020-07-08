# coding=utf-8
from unittest import TestCase

from snbpy.common.constant.exceptions import ConfigException
from snbpy.common.util.config_reader import read_config


class ConfigReaderTest(TestCase):
    def test_read_config(self):
        config = read_config('../../resource/test.config')
        self.assertIsNotNone(config)
        self.assertEqual(config.account, 'U123')
        self.assertEqual(config.key, '123')
        self.assertEqual(config.sign_type, 'Default')
        self.assertEqual(config.timeout, 1000)
        self.assertEqual(config.snb_server, 'localhost')
        self.assertEqual(config.snb_port, '8080')
        self.assertTrue(config.auto_login)
        config.verify()

    def test_invalid_config(self):
        config = read_config('../../resource/invalid.config')
        self.assertIsNotNone(config)
        self.assertEqual(config.account, 'U123')
        self.assertEqual(config.key, '123')
        self.assertEqual(config.sign_type, 'Default')
        self.assertEqual(config.timeout, 1000)
        self.assertEqual(config.snb_server, 'localhost')
        self.assertRaises(ConfigException, config.verify)
        self.assertEqual(config.snb_port, '')
        self.assertRaises(ConfigException, config.verify)
