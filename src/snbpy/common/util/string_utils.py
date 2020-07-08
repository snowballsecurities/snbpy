from snbpy.common.util.array_utils import ArrayUtils


class StringUtils(object):
    EMPTY = ""
    SPACE = " "

    @staticmethod
    def is_empty(string: str) -> bool:
        """
         * StringUtils.isEmpty(null)      = true
         * StringUtils.isEmpty("")        = true
         * StringUtils.isEmpty(" ")       = false
         * StringUtils.isEmpty("bob")     = false
         * StringUtils.isEmpty("  bob  ") = false

        :param string:
        :return:
        """
        return not bool(string)

    @staticmethod
    def is_not_empty(string: str) -> bool:
        """
         * StringUtils.isNotEmpty(null)      = false
         * StringUtils.isNotEmpty("")        = false
         * StringUtils.isNotEmpty(" ")       = true
         * StringUtils.isNotEmpty("bob")     = true
         * StringUtils.isNotEmpty("  bob  ") = true
        :param string:
        :return:
        """
        return bool(string)

    @staticmethod
    def is_blank(string: str) -> bool:
        """
         * StringUtils.isBlank(null)      = true
         * StringUtils.isBlank("")        = true
         * StringUtils.isBlank(" ")       = true
         * StringUtils.isBlank("bob")     = false
         * StringUtils.isBlank("  bob  ") = false
        :param string:
        :return:
        """
        return not bool(string) or not bool(string.strip())

    @staticmethod
    def is_not_blank(string: str) -> bool:
        """
         * StringUtils.isNotBlank(null)      = false
         * StringUtils.isNotBlank("")        = false
         * StringUtils.isNotBlank(" ")       = false
         * StringUtils.isNotBlank("bob")     = true
         * StringUtils.isNotBlank("  bob  ") = true
        :param string:
        :return:
        """
        return bool(string) and bool(string.strip())

    @staticmethod
    def is_any_empty(*strings) -> bool:
        """
         * StringUtils.isAnyEmpty(null)             = true
         * StringUtils.isAnyEmpty(null, "foo")      = true
         * StringUtils.isAnyEmpty("", "bar")        = true
         * StringUtils.isAnyEmpty("bob", "")        = true
         * StringUtils.isAnyEmpty("  bob  ", null)  = true
         * StringUtils.isAnyEmpty(" ", "bar")       = false
         * StringUtils.isAnyEmpty("foo", "bar")     = false

        :param strings:
        :return:
        """
        if ArrayUtils.is_empty(strings):
            return True
        for string in strings:
            if StringUtils.is_empty(string):
                return True
        return False

    @staticmethod
    def is_none_empty(*strings) -> bool:
        """
         * StringUtils.isNoneEmpty(null)             = false
         * StringUtils.isNoneEmpty(null, "foo")      = false
         * StringUtils.isNoneEmpty("", "bar")        = false
         * StringUtils.isNoneEmpty("bob", "")        = false
         * StringUtils.isNoneEmpty("  bob  ", null)  = false
         * StringUtils.isNoneEmpty(" ", "bar")       = true
         * StringUtils.isNoneEmpty("foo", "bar")     = true
        :param strings:
        :return:
        """
        return not StringUtils.is_any_empty(*strings)

    @staticmethod
    def is_any_blank(*strings) -> bool:
        """
         * StringUtils.isAnyBlank(null)             = true
         * StringUtils.isAnyBlank(null, "foo")      = true
         * StringUtils.isAnyBlank(null, null)       = true
         * StringUtils.isAnyBlank("", "bar")        = true
         * StringUtils.isAnyBlank("bob", "")        = true
         * StringUtils.isAnyBlank("  bob  ", null)  = true
         * StringUtils.isAnyBlank(" ", "bar")       = true
         * StringUtils.isAnyBlank("foo", "bar")     = false
        :param strings:
        :return:
        """
        if ArrayUtils.is_empty(strings):
            return True
        for string in strings:
            if StringUtils.is_blank(string):
                return True
        return False

    @staticmethod
    def is_none_blank(*strings) -> bool:
        """
         * StringUtils.isNoneBlank(null)             = false
         * StringUtils.isNoneBlank(null, "foo")      = false
         * StringUtils.isNoneBlank(null, null)       = false
         * StringUtils.isNoneBlank("", "bar")        = false
         * StringUtils.isNoneBlank("bob", "")        = false
         * StringUtils.isNoneBlank("  bob  ", null)  = false
         * StringUtils.isNoneBlank(" ", "bar")       = false
         * StringUtils.isNoneBlank("foo", "bar")     = true
        :param strings:
        :return:
        """
        return not StringUtils.is_any_blank(*strings)

    @staticmethod
    def default_string(string: str, default_string: str = "") -> str:
        """
         * StringUtils.defaultString(null)  = ""
         * StringUtils.defaultString("")    = ""
         * StringUtils.defaultString("bat") = "bat"
        """
        return default_string if StringUtils.is_empty(string) else string
