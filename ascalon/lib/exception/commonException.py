# -*- coding: utf-8 -*-
#
# 2019-09-17 liam
# 보통으로 쓰이는 사용자 정의 에러 집합

# 특정 타입의 객체를 무시합니다
class IgnoreType (Exception):
    def __init__ (self, location, type):
        self.type = str(type)
        self.location = str(location)
    def __str__ (self):
        return '[' + self.location + '] ' + self.type + u'타입 객체를 무시합니다 \n'