# -*- coding: utf-8 -*-
#
# 2019-09-18 liam
# 콘솔에서 확인하기 용도 [인코딩]

import logging
import sys
import re
from ascalon.lib.exception import commonException as ex

class ExtractEncoding ():
    def __init__ (self, location = None, object = None):
        try:
            ItemObject = None
            if re.search(r'[A-Z]\w+Item', str(type(object))) is not None:
                ItemObject = re.findall(r'[A-Z]\w+Item', str(type(object)))[0]

            if type(object) is str:
                self._disposeOfString(location = location, object = object)
            elif type(object) is int:
                self._disposeOfInteger(location = location, object = object)
            elif type(object) is float:
                self._disposeOfFloat(location = location, object = object)
            elif type(object) is dict:
                self._disposeOfDictionary(object = object)
            elif type(object) is list:
                pass
            elif type(object) is tuple:
                pass
            elif type(object) is bool:
                self._disposeOfBool(location = location, object = object)
            # elif type(object) is unicode:
            #     self._disposeOfUnicode(location = location, object = object)
            # elif type(object) is long:
            #     pass
            elif ItemObject is not None:
                self._disposeOfSpiderItem(object = object)
            elif object is None:
                raise ex.NotPermitThisType(type=type(object))
            else:
                pass
        except (Exception, ex.NotPermitThisType) as e:
            logging.error(e)

    def _disposeOfString (self, location, object):
        self._printer(location, __name__, sys._getframe().f_code.co_name, object)
    def _disposeOfInteger (self, location, object):
        self._printer(location, __name__, sys._getframe().f_code.co_name, object)
    def _disposeOfFloat (self, location, object):
        self._printer(location, __name__, sys._getframe().f_code.co_name, object)
    def _disposeOfDictionary (self, object):
        print(object)
    def _disposeOfList (self, object):
        print(object)
    def _disposeOfTuple (self, object):
        print(object)
    def _disposeOfBool (self, location, object):
        self._printer(location, __name__, sys._getframe().f_code.co_name, object)
    def _disposeOfUnicode (self, location, object):
        self._printer(location, __name__, sys._getframe().f_code.co_name, object)
    def _disposeOfSpiderItem (self, object):
        self._printerByIterator(__name__, sys._getframe().f_code.co_name, object)


    def _printer (self, location, moduleLocation, methods, object):
        print('[' + moduleLocation + ' -> ' + methods + ']')
        if location is not None:
            print('[' + str(type(object)) + '][' + location + '] ' + str(object) + '\n')
        else:
            print('[value] ' + str(object) + '\n')
    def _printerByIterator (self, moduleLocation, methods, object):
        print('[' + moduleLocation + ' -> ' + methods + ']')
        for key, val in object.items():
            print('[' + str(type(val)) + '][' + key + '] ' + str(val))
        print('\n')