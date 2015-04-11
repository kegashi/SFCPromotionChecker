#!/usr/bin/python
# -*- coding: utf-8 -*-

import cgitb
cgitb.enable()

# CGI Test
import cgi

print "Content-Type: text/html\n\n"

print "<html lang=\"ja\"><head><meta charset=\"UTF-8\"><title>SFC 進学要件確認</title></head><body bgcolor=\"#cbd7e4\">"

form = cgi.FieldStorage()
form_ok = 0
if form.has_key("gakubu") and form.has_key("zaiseki") :
	form_ok = 1
if form_ok == 0 :
	print "<h1>ERROR</h1>"
else :
	grade2 = 0
	grade3 = 0
	grade4 = 0
	grade5 = 0
	list = [0, 0, 0, 0, 0, 0, 0, 0, 0]
	#01
	list[0] = int(form["part111"].value)
	#02
	list[1] = int(form["part211"].value)
	#03
	prog = [0, 0, 0, 0, 0]
	prog[0] = int(form["part331"].value)
	prog[1] = int(form["part332"].value)
	prog[2] = int(form["part333"].value)
	prog[3] = int(form["part334"].value)
	prog[4] = int(form["part335"].value)
	part0303 = 0
	prog_check = 0
	for num in range(0,5):
		part0303 += prog[num]
		if prog[num] == 0:
			prog_check = prog_check + 1
	part0305 = int(form["part351"].value) + int(form["part352"].value) + int(form["part353"].value) + int(form["part354"].value) + int(form["part355"].value) + int(form["part356"].value) + int(form["part357"].value) + int(form["part358"].value) + int(form["part359"].value) + int(form["part3510"].value) + int(form["part3511"].value)
	part0306 = int(form["part361"].value) + int(form["part362"].value)
	list[2] = int(form["part311"].value) + int(form["part321"].value) + part0303 + int(form["part341"].value) + part0305 + part0306 + int(form["part371"].value)
	#04
	list[3] = int(form["part411"].value) + int(form["part421"].value) + int(form["part429"].value) + int(form["part431"].value) + int(form["part439"].value)
	#05
	list[4] = int(form["part511"].value) + int(form["part512"].value) + int(form["part513"].value)
	#06
	list[5] = int(form["part619"].value)
	#07
	list[6] = int(form["part711"].value)
	#60
	list[7] = int(form["part6011"].value)
	if int(form["part6011"].value) > 20:
		list[7] = 20
	#90
	list[8] = int(form["part9011"].value) + int(form["part9092"].value)
	sum = 0
	for num in range(0,8):
		sum += list[num]
	#	print str(num) + " = " + str(list[num]) + "<br>"
	#print sum
	others = int(form["part429"].value) + int(form["part439"].value) + int(form["part619"].value)
	if others > 60:
		sum = sum - others + 60
	part1 = int(form["zaiseki"].value)
	print "<h2><font color=\"#00f\">R</font><font color=\"#f00\">E</font><font color=\"#00f\">S</font><font color=\"#f00\">U</font><font color=\"#00f\">L</font><font color=\"#f00\">T</font></h2><hr><p>"
	print "<h3>基本情報</h3><p>"
	if form["gakubu"].value == "1":
		print "学部: 総合政策学部<br />"
	if form["gakubu"].value == "2":
		print "学部: 環境情報学部<br />"
	print "在籍数: " + form["zaiseki"].value + "<br />"
	print "取得単位数: " + str(sum) + "<br /><hr>" 
	
	print "<h3>第2学年進学要件</h3><p>"
	if int(form["zaiseki"].value) < 2:
		zaiseki_husoku = 2 - int(form["zaiseki"].value)
		print "在籍学期数「" + str(zaiseki_husoku) + "」不足<br>"
		grade2 = 1
	if sum < 30:
		tani_husoku = 30 - sum
		print "合計単位数「" + str(tani_husoku) + "」不足<br />"
		grade2 = 1
	if int(form["part111"].value) < 2:
		print "総合口座科目「2」不足<br />"
		grade2 = 1
	if int(form["part311"].value) < 2:
		print "創造実践科目「2」不足<br />"
		grade2 = 1
	if int(form["part411"].value) < 2:
		print "先端発見科目「2」不足<br />"
		grade2 = 1
	if grade2 == 0:
		print "<h4>進級</h4>"
	print "<hr><h3>第3学年進学要件</h3><p>"
	if int(form["zaiseki"].value) < 4:
                zaiseki_husoku = 4 - int(form["zaiseki"].value)
                print "在籍学期数「" + str(zaiseki_husoku) + "」不足<br>"
		grade3 = 1
	if sum < 30:
                tani_husoku = 60 - sum
		print "合計単位数「" + str(tani_husoku) + "」不足<br />"
		grade3 = 1
	if grade3 == 0:
		print "<h4>進級</h4>"
	print "<hr><h3>第4学年進学要件</h3><p>"
	if int(form["zaiseki"].value) < 6:
                zaiseki_husoku = 6 - int(form["zaiseki"].value)
                print "在籍学期数「" + str(zaiseki_husoku) + "」不足<br>"
		grade4 = 1
	if int(form["part341"].value) < 4:
		part341_husoku = 4 -int(form["part341"].value)
		grade4 = 1
	if int(form["part371"].value) < 2:
		print "創造誘発科目「2」不足<br />"
		grade4 = 1
	if form["gakubu"].value == "1":
		if part0303 < 4:
			part0303_husoku = 4 - part0303
			print "プログラミング「" + str(part0303_husoku)  + "」不足<br />"
			grade4 = 1
		if part0305 < 4:
			part0305_husoku = 4 - part0305
			print "言語コミュニケーション「" + str(part0305_husoku) + "」不足<br />"
	if form["gakubu"].value == "2":
		if part0303 < 8:
			part0303_husoku = 8 - part0303
			print "プログラミング「" + str(part0303_husoku) + "」不足<br />"
			grade4 = 1
		if prog_check > 3:
			print "プログラミング科目が2系列以上から取得できていません<br />"
			grade4 = 1
	if int(form["part361"].value) < 1:
		print "心身ウェルネス「1」不足<br />"
		grade4 = 1
	if int(form["part362"].value) < 3:
		part362_husoku = 3 - int(form["part362"].value)
		print "体育「" + str(part362_husoku) + "」不足<br />"
		grade4 = 1
	if int(form["part511"].value) < 2:
		print "研究会「2」不足<br />"
		grade4 = 1
	if grade4 == 0:
		print "<h4>進級</h4>"
	if form["gakubu"].value == "1":
		print "(一部の科目は、創造技法言語コミュニケーション科目の 4 単位に含めることができません)<br>"
	print "<hr><h3>卒業要件</h3><p>"
	if int(form["zaiseki"].value) < 8:
                zaiseki_husoku = 8 - int(form["zaiseki"].value)
                print "在籍学期数「" + str(zaiseki_husoku) + "」不足<br>"
		grade5 = 1
	if sum < 124:
		tani_husoku = 124 - sum
		print "合計単位数「" + str(tani_husoku) + "」不足<br>"
		grade5 = 1
	if int(form["part512"].value) <4:
		part512_husoku = 4 - int(form["part512"].value)
		print "卒業プロジェクト「" + str(part512_husoku) + "」不足"
	if grade5 == 0:
		print "<h4>卒業</h4>"


print "</body></html>"
