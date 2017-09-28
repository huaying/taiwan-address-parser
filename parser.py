import re

test = '''
新竹市武陵路61巷1弄28號 台北市南港路66號
新北市三重區正義南路36巷9號
新北市永和區永平路170號
台中市西區美村路一段111號 台中市西區美村路一段149巷12號
台中市西區忠誠街91號 台中市北區太平路63巷1號
台中市南屯區惠文路328號
台北市中正區汀州路三段165號 台南市安平區安平路418號 台中市北區三民路三段201巷14號
台中市烏日區學田路8巷68號 台南市中西區民族路二段160號 台北市信義區松壽路12號3樓
台中市南屯區懷德街59巷6號 台中市西屯區文華路7號之1 台北市松山區南京東路五段291巷29弄7號2樓
'''

aa = '''
—
🔺三重蛋餅王🔺
—
✔️雙蛋蛋餅$40 —
沒有明顯的招牌但生意卻非常的好！店裡有分蔥油餅、蛋餅、雙蛋，皆是以蔥油餅為基底，沒有蛋🥚、一顆蛋🥚、兩顆🥚做為區別，搭配獨家醬料～雖然炸過可是吃起來不油膩😍😍還帶點QQ又甜甜的口感！！
不虧是男神 @raymond.hou 說的三重蕭賀甲蛋餅👍🏻👍🏻👍🏻👍🏻👍🏻👍🏻
························································
····
🏘新北市三重區正義南路36巷9號台北市和平西路一段81號

🕰平日6:00-10:30/週末6:00-11:30
····························································
🔴Fb粉專、痞克邦🔎菲比的食物日常
👇🏻看更多台北美食
#菲比吃台北
'''

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

addr_main = '[%s]\w+?[路|街].*?\d{1,5}號' % '|'.join(city + other_city)
addr_optional = '(?:\d{1,3}樓)?(?:\d{1,3}室)?(?:[\-|之]\d{1,2})?'
pattern = addr_main + addr_optional
a = re.findall(pattern, aa)
print(a, len(a))