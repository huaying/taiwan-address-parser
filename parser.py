# coding:utf-8
import re


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


def parse(text):
    '''
        input: text(str)
        output: a list of address(array)
    '''
    addr_main = u'[%s]\w+?[路|街]\w*?\d{1,5}號' % '|'.join(city + other_city)
    addr_optional = u'(?:\d{1,3}樓)?(?:\d{1,3}室)?(?:[\-|之]\d{1,2})?'
    pattern = addr_main + addr_optional
    return re.findall(pattern, text, re.UNICODE)
