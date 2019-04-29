#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Licensed under WTFPL or the Unlicense or CC0.
# This uses Python 3, but it's easy to port to Python 2 by changing
# strings to u'xx'.

import itertools
import random
import sys


def num2chinese(num, big=False, simp=True, o=False, twoalt=False):
    """
    Converts numbers to Chinese representations.
    `big`   : use financial characters.
    `simp`  : use simplified characters instead of traditional characters.
    `o`     : use 〇 for zero.
    `twoalt`: use 两/兩 for two when appropriate.
    Note that `o` and `twoalt` is ignored when `big` is used, 
    and `twoalt` is ignored when `o` is used for formal representations.
    """
    # check num first
    nd = str(num)
    if abs(float(nd)) >= 1e48:
        raise ValueError('number out of range')
    elif 'e' in nd:
        raise ValueError('scientific notation is not supported')
    c_symbol = '正负点' if simp else '正負點'
    if o:  # formal
        twoalt = False
    if big:
        c_basic = '零壹贰叁肆伍陆柒捌玖' if simp else '零壹貳參肆伍陸柒捌玖'
        c_unit1 = '拾佰仟'
        c_twoalt = '贰' if simp else '貳'
    else:
        c_basic = '〇一二三四五六七八九' if o else '零一二三四五六七八九'
        c_unit1 = '十百千'
        if twoalt:
            c_twoalt = '两' if simp else '兩'
        else:
            c_twoalt = '二'
    c_unit2 = '万亿兆京垓秭穰沟涧正载' if simp else '萬億兆京垓秭穰溝澗正載'
    revuniq = lambda l: ''.join(k for k, g in itertools.groupby(reversed(l)))
    nd = str(num)
    result = []
    if nd[0] == '+':
        result.append(c_symbol[0])
    elif nd[0] == '-':
        result.append(c_symbol[1])
    if '.' in nd:
        integer, remainder = nd.lstrip('+-').split('.')
    else:
        integer, remainder = nd.lstrip('+-'), None
    if int(integer):
        splitted = [integer[max(i - 4, 0):i]
                    for i in range(len(integer), 0, -4)]
        intresult = []
        for nu, unit in enumerate(splitted):
            # special cases
            if int(unit) == 0:  # 0000
                intresult.append(c_basic[0])
                continue
            elif nu > 0 and int(unit) == 2:  # 0002
                intresult.append(c_twoalt + c_unit2[nu - 1])
                continue
            ulist = []
            unit = unit.zfill(4)
            for nc, ch in enumerate(reversed(unit)):
                if ch == '0':
                    if ulist:  # ???0
                        ulist.append(c_basic[0])
                elif nc == 0:
                    ulist.append(c_basic[int(ch)])
                elif nc == 1 and ch == '1' and unit[1] == '0':
                    # special case for tens
                    # edit the 'elif' if you don't like
                    # 十四, 三千零十四, 三千三百一十四
                    ulist.append(c_unit1[0])
                elif nc > 1 and ch == '2':
                    ulist.append(c_twoalt + c_unit1[nc - 1])
                else:
                    ulist.append(c_basic[int(ch)] + c_unit1[nc - 1])
            ustr = revuniq(ulist)
            if nu == 0:
                intresult.append(ustr)
            else:
                intresult.append(ustr + c_unit2[nu - 1])
        result.append(revuniq(intresult).strip(c_basic[0]))
    else:
        result.append(c_basic[0])
    if remainder:
        result.append(c_symbol[2])
        result.append(''.join(c_basic[int(ch)] for ch in remainder))
    return ''.join(result)



def chongzhen(num):
	cz_years = []
	random_num1 = random.randint(0,5)
	event_year = [1628,1840,1949,1982,1989,65535]
	sexagenary = ['甲子', '乙丑', '丙寅', '丁卯', '戊辰', '己巳', '庚午', '辛未', '壬申', '癸酉', '甲戌', '乙亥', '丙子', '丁丑', '戊寅', '己卯', '庚辰', '辛巳', '壬午', '癸未', '甲申', '乙酉', '丙戌', '丁亥', '戊子', '己丑', '庚寅', '辛卯', '壬辰', '癸巳', '甲午', '乙未', '丙申', '丁酉', '戊戌', '己亥', '庚子', '辛丑', '壬寅', '癸卯', '甲辰', '乙巳', '丙午', '丁未', '戊申', '己酉', '庚戌', '辛亥', '壬子', '癸丑', '甲寅', '乙卯', '丙辰', '丁巳', '戊午', '己未', '庚申', '辛酉', '壬戌', '癸亥']
	for i in range(0, 59):
	 cz_years.append(event_year[random_num1] + i)
	 
	left = (num - event_year[random_num1])%60
	loop = int((num - event_year[random_num1] - left)/60 + 1) 
	left1628 = left + 4
	if left1628 > 59: 
	 left1628 -= 60
	left1840 = left + 36
	if left1840 > 59: 
	 left1840 -= 60
	left1949 = left + 25
	if left1949 > 59: 
	 left1949 -= 60
	left1982 = left + 58
	if left1982 > 59: 
	 left1982 -= 60
	left1989 = left + 5
	if left1989 > 59: 
	 left1989 -= 60
	event_string = ['皇明崇禎後', '皇明崇禎後肆庚子','皇明崇禎後陸己丑', '皇明崇禎後陸壬戌', '皇明崇禎後柒己巳']

	
	#print(left)
	#print(loop)

	
	#print(sexagenary[left])

	if random_num1 == 0:
	 return event_string[random_num1] + num2chinese(loop, True, False) + sexagenary[left1628] + '年'
	elif random_num1 == 1:
	 return event_string[random_num1] + num2chinese(loop, True, False) + sexagenary[left1840] + '年'
	elif random_num1 == 2:
	 return event_string[random_num1] + num2chinese(loop, True, False) + sexagenary[left1949] + '年'
	elif random_num1 == 3:
	 return event_string[random_num1] + num2chinese(loop, True, False) + sexagenary[left1982] + '年'
	elif random_num1 == 4:
	 return event_string[random_num1] + num2chinese(loop, True, False) + sexagenary[left1989] + '年'
	else:
	 return '皇明崇禎' + num2chinese(num - 1628, True, False) + '年'
print(chongzhen(int(sys.argv[1])))
#print(sys.argv)
 
