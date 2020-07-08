# coding=utf-8
class ArrayUtils(object):
    @staticmethod
    def is_empty(array: tuple or list) -> bool:
        return array is None or len(array) == 0
