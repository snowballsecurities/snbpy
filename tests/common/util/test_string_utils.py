from unittest import TestCase

from snbpy.common.util.string_utils import StringUtils


class TestStringUtils(TestCase):
    def test_is_empty(self):
        self.assertTrue(StringUtils.is_empty(None))
        self.assertTrue(StringUtils.is_empty(""))
        self.assertFalse(StringUtils.is_empty(" "))
        self.assertFalse(StringUtils.is_empty("bob"))
        self.assertFalse(StringUtils.is_empty("  bob  "))

    def test_is_not_empty(self):
        self.assertFalse(StringUtils.is_not_empty(None))
        self.assertFalse(StringUtils.is_not_empty(""))
        self.assertTrue(StringUtils.is_not_empty(" "))
        self.assertTrue(StringUtils.is_not_empty("bob"))
        self.assertTrue(StringUtils.is_not_empty("  bob  "))

    def test_is_blank(self):
        self.assertTrue(StringUtils.is_blank(None))
        self.assertTrue(StringUtils.is_blank(""))
        self.assertTrue(StringUtils.is_blank(" "))
        self.assertFalse(StringUtils.is_blank("bob"))
        self.assertFalse(StringUtils.is_blank("  bob  "))

    def test_is_not_blank(self):
        self.assertFalse(StringUtils.is_not_blank(None))
        self.assertFalse(StringUtils.is_not_blank(""))
        self.assertFalse(StringUtils.is_not_blank(" "))
        self.assertTrue(StringUtils.is_not_blank("bob"))
        self.assertTrue(StringUtils.is_not_blank("  bob  "))

    def test_is_any_empty(self):
        self.assertTrue(StringUtils.is_any_empty(None))
        self.assertTrue(StringUtils.is_any_empty(None, "foo"))
        self.assertTrue(StringUtils.is_any_empty("", "foo"))
        self.assertTrue(StringUtils.is_any_empty("bob", None))
        self.assertTrue(StringUtils.is_any_empty("  bob  ", None))
        self.assertFalse(StringUtils.is_any_empty(" ", "bar"))
        self.assertFalse(StringUtils.is_any_empty("foo", "bar"))

    def test_is_none_empty(self):
        self.assertFalse(StringUtils.is_none_empty(None))
        self.assertFalse(StringUtils.is_none_empty(None, "foo"))
        self.assertFalse(StringUtils.is_none_empty("", "foo"))
        self.assertFalse(StringUtils.is_none_empty("bob", None))
        self.assertFalse(StringUtils.is_none_empty("  bob  ", None))
        self.assertTrue(StringUtils.is_none_empty(" ", "bar"))
        self.assertTrue(StringUtils.is_none_empty("foo", "bar"))

    def test_is_any_blank(self):
        self.assertTrue(StringUtils.is_any_blank(None))
        self.assertTrue(StringUtils.is_any_blank(None, "foo"))
        self.assertTrue(StringUtils.is_any_blank("", "foo"))
        self.assertTrue(StringUtils.is_any_blank("bob", None))
        self.assertTrue(StringUtils.is_any_blank("  bob  ", None))
        self.assertTrue(StringUtils.is_any_blank(" ", "bar"))
        self.assertFalse(StringUtils.is_any_blank("foo", "bar"))

    def test_is_none_blank(self):
        self.assertFalse(StringUtils.is_none_blank(None))
        self.assertFalse(StringUtils.is_none_blank(None, "foo"))
        self.assertFalse(StringUtils.is_none_blank("", "foo"))
        self.assertFalse(StringUtils.is_none_blank("bob", None))
        self.assertFalse(StringUtils.is_none_blank("  bob  ", None))
        self.assertFalse(StringUtils.is_none_blank(" ", "bar"))
        self.assertTrue(StringUtils.is_none_blank("foo", "bar"))

    def test_default_string(self):
        self.assertEquals("", StringUtils.default_string(None))
        self.assertEquals("", StringUtils.default_string(""))
        self.assertEquals(" ", StringUtils.default_string(" "))
        self.assertEquals("bat", StringUtils.default_string("bat"))
