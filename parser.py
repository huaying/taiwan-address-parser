# coding:utf-8
from future.standard_library import install_aliases
install_aliases() # noqa

import json
import re
from urllib.request import urlopen
from urllib.parse import quote
from io import open


city = [
    u'台北市', u'新北市', u'基隆市', u'宜蘭縣',
    u'新竹市', u'新竹縣', u'桃園市', u'苗栗縣',
    u'台中市', u'彰化縣', u'南投縣', u'雲林縣',
    u'嘉義市', u'嘉義縣', u'台南市', u'高雄市',
    u'屏東縣', u'台東縣', u'花蓮縣', u'澎湖縣',
    u'金門縣', u'連江縣'
]
other_city = [
    u'台北縣', u'高雄縣', u'臺北市', u'臺北縣',
    u'台中縣', u'臺中市', u'臺中縣'
]


def get_geocode(address):
    geocode_api = 'http://maps.googleapis.com/maps/api/geocode/json?address='
    with urlopen(geocode_api + quote(address)) as geocode:
        res = json.loads(geocode.read().decode('utf-8'))

        if res and res['status'] == 'OK':
            result = res['results'][0]
            geometry = result['geometry']
            formatted_address = result['formatted_address']
            is_tw_address = (
                geometry['location_type'] != 'APPROXIMATE' and
                'Taiwan' in formatted_address
            )
            if is_tw_address:
                return geometry['location']
        return None


def extract_address(text):
    '''
        input: text(str)
        output: a list of address(array)
    '''
    addr_main = u'[%s]\w+?[路|街]\w*?\d{1,5}號' % '|'.join(city + other_city)
    addr_optional = u'(?:\d{1,3}樓)?(?:\d{1,3}室)?(?:[\-|之]\d{1,2})?'
    pattern = addr_main + addr_optional
    return re.findall(pattern, text, re.UNICODE)


def url_extract_address(url):
    with urlopen(url) as f:
        text = f.read().decode('utf-8')
        return extract_address(text)


def file_extract_address(filepath):
    with open(filepath, encoding='utf-8') as f:
        text = f.read()
        return extract_address(text)
