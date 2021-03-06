# coding:utf-8
from parser import extract_address
from parser import url_extract_address
from parser import file_extract_address
from parser import get_geocode
import os


def test_many_address():
    address_str = u'''
    新竹市武陵路61巷1弄28號 台北市南港路66號
    新北市三重區正義南路36巷9號
    新北市永和區永平路170號
    台中市西區美村路一段111號 台中市西區美村路一段149巷12號
    台中市西區忠誠街91號 台中市 小台中市北區太平路63巷1號
    台中市南屯區惠文路328號
    台北市中正區汀州路三段165號 台中市的某段路上 台南市安平區安平路418號
    台中市北區三民路三段201巷14號
    台中市烏日區學田路8巷68號 台南 台南市中西區民族路二段160號 台北市信義區松壽路12號3樓
    台中市南屯區懷德街59巷6號 台中市西屯區文華路7號之1 臺北
    台北市松山區南京東路五段291巷29弄7號2樓
    '''
    expect = [
        u'新竹市武陵路61巷1弄28號',
        u'台北市南港路66號',
        u'新北市三重區正義南路36巷9號',
        u'新北市永和區永平路170號',
        u'台中市西區美村路一段111號',
        u'台中市西區美村路一段149巷12號',
        u'台中市西區忠誠街91號',
        u'台中市北區太平路63巷1號',
        u'台中市南屯區惠文路328號',
        u'台北市中正區汀州路三段165號',
        u'台南市安平區安平路418號',
        u'台中市北區三民路三段201巷14號',
        u'台中市烏日區學田路8巷68號',
        u'台南市中西區民族路二段160號',
        u'台北市信義區松壽路12號3樓',
        u'台中市南屯區懷德街59巷6號',
        u'台中市西屯區文華路7號之1',
        u'台北市松山區南京東路五段291巷29弄7號2樓',
    ]
    res = extract_address(address_str)
    assert len(res) == len(expect)
    assert res == expect


def test_ig_post():
    instagram_post = u'''
    —
    🔺三重蛋餅王🔺
    —
    ✔️雙蛋蛋餅$40 —
    沒有明顯的招牌但生意卻非常的好！店裡有分蔥油餅、蛋餅、雙蛋，皆是以蔥油餅為基底，沒有蛋🥚、一顆蛋🥚、兩顆🥚做為區別，搭配獨家醬料～雖然炸過可是吃起來不油膩😍😍還帶點QQ又甜甜的口感！！
    不虧是男神 @raymond.hou 說的三重蕭賀甲蛋餅👍🏻👍🏻👍🏻👍🏻👍🏻👍🏻
    ························································
    ····
    🏘新北市三重區正義南路36巷9號

    🕰平日6:00-10:30/週末6:00-11:30
    ····························································
    🔴Fb粉專、痞克邦🔎菲比的食物日常
    👇🏻看更多台北美食
    #菲比吃台北
    '''
    expect = [u'新北市三重區正義南路36巷9號']
    res = extract_address(instagram_post)
    assert len(res) == len(expect)
    assert res == expect


def test_parse_file():
    curdir = os.path.dirname(os.path.realpath(__file__))
    res = file_extract_address('%s/file.txt' % curdir)
    assert len(res) == 18


def test_parse_url():
    url = 'http://iko40623.pixnet.net/blog/post/434453072'
    res = url_extract_address(url)
    assert res == [u'台南市東區長榮路二段63號']


def test_get_geocode():
    expect = {u'lat': 25.0529774, u'lng': 121.5664644}
    res = get_geocode('台北市松山區南京東路五段291巷29弄7號2樓')
    assert res['lat'] == expect['lat']
    assert res['lng'] == expect['lng']
