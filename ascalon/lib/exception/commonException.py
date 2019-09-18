# -*- coding: utf-8 -*-
#
# 2019-09-17 liam
# 보통으로 쓰이는 사용자 정의 에러 집합

# 특정 타입의 객체를 무시합니다
class IgnoreType (Exception):
    def __init__ (self, location = None, type = ''):
        self.type = str(type)
        if location is not None:
            self.location = str(location)
    def __str__ (self):
        if self.location is not None:
            return '[' + self.location + '] ' + self.type + u'타입 객체를 무시합니다 \n'
        else:
            return self.type + u'타입 객체를 무시합니다 \n'

# 특정 타입의 객체를 허용시키지 않는다
class NotPermitThisType (Exception):
    def __init__ (self, location = None, type = ''):
        self.type = str(type)
        if location is not None:
            self.location = str(location)
        else:
            self.location = None
    def __str__ (self):
        if self.location is not None:
            return '[' + self.location + '] ' + self.type + u' 해당 객체는 허용되지 않습니다 \n'
        else:
            return self.type + u' 해당 객체는 허용되지 않습니다 \n'