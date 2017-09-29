import re


city = [
    '台北市', '新北市', '基隆市','宜蘭縣',
    '新竹市', '新竹縣', '桃園市','苗栗縣',
    '台中市', '彰化縣', '南投縣','雲林縣',
    '嘉義市', '嘉義縣', '台南市','高雄市',
    '屏東縣', '台東縣', '花蓮縣','澎湖縣',
    '金門縣', '連江縣'
]
other_city = [
    '台北縣', '高雄縣', '臺北市', '臺北縣',
    '台中縣', '臺中市', '臺中縣'
]


def parse(text):
    '''
        input: text(str)
        output: a list of address(array)
    '''
    addr_main = '[%s]\w+?[路|街]\w*?\d{1,5}號' % '|'.join(city + other_city)
    addr_optional = '(?:\d{1,3}樓)?(?:\d{1,3}室)?(?:[\-|之]\d{1,2})?'
    pattern = addr_main + addr_optional
    return re.findall(pattern, text)
