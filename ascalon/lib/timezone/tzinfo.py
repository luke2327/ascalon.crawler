# -*- coding: utf-8 -*-
#
# 2019-10-06 liam
# 각 나라별 TIMEZONE

import pytz

TZINFO = {
  'UTC': pytz.timezone('UTC'),
  'KST': pytz.timezone('Asia/Seoul'),
  'JST': pytz.timezone('Asia/Tokyo'),
}