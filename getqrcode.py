
import random
import time
import requests
import functools
import json
import os
import pickle

from lxml import etree
from jd_logger import logger
from timer import Timer
from config import global_config
from concurrent.futures import ProcessPoolExecutor
from exception import SKException
from util import (
    parse_json,
    send_wechat,
    wait_some_time,
    response_status,
    save_image,
    open_image
)

logger.info('开始获取验证码图片')
url = 'https://qr.m.jd.com/show'
payload = {
            'appid': 133,
            'size': 147,
            't': str(int(time.time() * 1000)),
        }
headers = {
            'User-Agent': global_config.getRaw('config', 'DEFAULT_USER_AGENT'),
            'Referer': 'https://passport.jd.com/new/login.aspx',
        }
resp =requests.session().get(url=url, headers=headers, params=payload)
save_image(resp, 'qrcode.png')
