# coding=utf-8
# Create date: November 7, 2020
# Author: Huiqin Gao

import random
mark = list()
nbr = list()
gua_nbr = ""
gua = dict()

gua = {
    "111111": "1, 乾为, 天",
    "000000": "2, 坤为, 地",
    "100010": "3, 水雷, 屯",
    "010001": "4, 山水, 蒙",
    "111010": "5, 水天, 需",
    "010111": "6, 天水, 讼",
    "010000": "7, 地水, 师",
    "000010": "8, 水地, 比",
    "111011": "9, 风天, 小畜",
    "110111": "10, 天泽, 履",
    "111000": "11, 地天, 泰",
    "000111": "12, 天地, 否",
    "101111": "13, 天火, 同人",
    "111101": "14, 火天, 大有",
    "001000": "15, 地山, 谦",
    "000100": "16, 雷地, 豫",
    "100110": "17, 泽雷, 随",
    "011001": "18, 山风, 蛊",
    "110000": "19, 地泽, 临",
    "000011": "20, 风地, 观",
    "100101": "21, 火雷, 噬嗑",
    "101001": "22, 山火, 贲",
    "000001": "23, 山地, 剥",
    "100000": "24, 地雷, 复",
    "100111": "25, 天雷, 无妄",
    "111001": "26, 山天, 大畜",
    "100001": "27, 山雷, 颐",
    "011110": "28, 泽风, 大过",
    "010010": "29, 坎为, 水",
    "101101": "30, 离为, 火",
    "001110": "31, 泽山, 咸",
    "011100": "32, 雷风, 恒",
    "001111": "33, 天山, 遁",
    "111100": "34, 雷天, 大壮",
    "000101": "35, 火地, 晋",
    "101000": "36, 地火, 明夷",
    "101011": "37, 风火, 家人",
    "110101": "38, 火泽, 睽",
    "001010": "39, 水山, 蹇",
    "010100": "40, 雷水, 解",
    "110001": "41, 山泽, 损",
    "100011": "42, 风雷, 益",
    "111110": "43, 泽天, 夬",
    "011111": "44, 天风, 姤",
    "000110": "45, 泽地, 萃",
    "011000": "46, 地风, 升",
    "010110": "47, 泽水, 困",
    "011010": "48, 水风, 井",
    "101110": "49, 泽火, 革",
    "011101": "50, 火风, 鼎",
    "100100": "51, 震为, 雷",
    "001001": "52, 艮为, 山",
    "001011": "53, 风山, 渐",
    "110100": "54, 雷泽, 归妹",
    "101100": "55, 雷火, 丰",
    "001101": "56, 火山, 旅",
    "011011": "57, 巽为, 风",
    "110110": "58, 兑为, 泽",
    "010011": "59, 风水, 涣",
    "110010": "60, 水泽, 节",
    "110011": "61, 风泽, 中孚",
    "001100": "62, 雷山, 小过",
    "101010": "63, 水火, 既济",
    "010101": "64, 火水, 未济"
}

def yao():
    r1 = random.randint(2,3)
    r2 = random.randint(2,3)
    r3 = random.randint(2,3)
    sum = r1 + r2 + r3
    yinyang = ''
    if sum == 9:
        yinyang = '老阳'
    elif sum == 8:
        yinyang = '少阴'
    elif sum == 7:
        yinyang = '少阳'
    elif sum == 6:
        yinyang = '老阴'

    return yinyang

def yao_image(yao):
    if '阳' in yao:
        return '▇▇▇▇▇▇▇▇▇▇▇▇▇▇'
    elif '阴' in yao:
        return '▇▇▇▇▇▇  ▇▇▇▇▇▇'

def yao_nbr(yao):
    if '阳' in yao:
        return 1
    elif '阴' in yao:
        return 0

for x in range (6):
    y_order = x+1
    y = yao()
    y_nbr = yao_nbr(y)
    yao_str = '第' + str(y_order) + '爻：' + y + '   ' + yao_image(y)
    mark.append(yao_str)
    nbr.append(y_nbr)

for x in range(6):
    gua_nbr += str(nbr[x])

print "=========================="
print gua[gua_nbr]
print "=========================="
print mark[5]
print mark[4]
print mark[3]
print mark[2]
print mark[1]
print mark[0]
