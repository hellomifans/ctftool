#基于python3的一些简单函数，不需要另外安装库，应该还会持续更新。
#本人小弱鸡，有问题也希望大家及时指正。

import base64
# import base91
import os
import sys
import hashlib
sys.setrecursionlimit(1000000)


#base64,第二个参数为模式，默认为解码，当flg为0时为编码
def B64(s,flg=1):
	if (flg !=0):
		return(base64.b64decode(s)).decode()
	else:
		return(base64.b64encode(bytes(s.encode("utf-8"))))

		
#base32,第二个参数为模式，默认为解码，当flg为0时为编码	
def B32(s,flg=1):
	if (flg !=0):
		return(base64.b32decode(s)).decode()
	else:
		return(base64.b32encode(bytes(s.encode("utf-8"))))

		
#base16,即hex,第二个参数为模式，默认为解码，当flg为0时为编码
def B16(s,flg=1):
	if (flg !=0):
		return(base64.b16decode(s.upper())).decode()
	else:
		return(base64.b16encode(bytes(s.encode("utf-8"))))

		
#base91,第二个参数为模式，默认为解码，当flg为0时为编码，需要自己安装库
# def B91(s,flg=1):
	# if (flg !=0):
		# return(base91.decode(s)).decode()
	# else:
		# return(base91.encode(bytes(s.encode("utf-8"))))

		
#凯撒密码，即移位密码，返回值为所有移位后结果组成的字典
def CASER(s):
	kslist=list(s)
	result=[]
	for ksn1 in range(26):
		for ksn2 in range(len(s)):
			if "a"<=kslist[ksn2]<="z" or "A"<=kslist[ksn2]<="Z":
				if kslist[ksn2]=="z" or kslist[ksn2]=="Z":
					kslist[ksn2]=chr(ord(kslist[ksn2])-25)
				else:
					kslist[ksn2]=chr(ord(kslist[ksn2])+1)
		kss="".join(kslist)
		result.append(kss)
	return result

	
#字符串逆序	
def REV(s):
	return(''.join(reversed(list(s))))
	

#十六进制转为二进制，输入输出皆为字符串
def H2B(s):
	temp=bin(eval("0x"+s))[2:]
	for i in range(len(s)*4-len(temp)):
		temp ="0"+temp
	return temp


#二进制转为十六进制，输入输出皆为字符串	
def B2H(s):
	temp=hex(eval("0b"+s))[2:]
	for i in range(len(s)//4-len(temp)):
		temp ="0"+temp
	return temp
	

#栅栏，输出为所有栏数序列组成的数组
def FENSE(s):
	slist=[]
	for i in range(len(s)):
		s1=""
		for j in range(i):
			s1+=s[j::i]
		slist.append(s1)
	slist.pop(0)
	return slist

	
#二进制转字符串，	
def B2S(s):
	ss=""
	for i in range(len(s)//8):
		ss+=chr(eval("0b"+s[:8]))
		s=s[8:]
	return ss


#清屏，无返回值	
def CLS():
	try:
		os.system("cls")
	except:
		os.system("clear")


#求逆，自己用穷举瞎**写的函数，输入值不要过大，不然跑不出来的 (*/ω＼*)		
def NI(a,b):
	for i in range(b):
		if ((1+b*i)%a==0) and ((1+b*i)//a<=b):
			return (1+b*i)//a
			

#求最大公因数			
def GCD(a,b):
    if a%b == 0:
        return b
    else :
        return GCD(b,a%b)
		
#返回输入的MD5值		
def MD5(s):
	s=bytes(s.encode("utf-8"))
	return hashlib.md5(s).hexdigest()
	
#返回输入的sha1值		
def SHA1(s):
	s=bytes(s.encode("utf-8"))
	return hashlib.sha1(s).hexdigest()
	
#返回输入的sha256值		
def SHA256(s):
	s=bytes(s.encode("utf-8"))
	return hashlib.sha256(s).hexdigest()
	

#判断输入字符串中包含的数据类型，返回值为列表，其中ALPH为大写字母，alph为小写字母	
def TYPE(s):
	result=[]
	num="0123456789"
	alph="qwertyuiopasdfghjklzxcvbnm"
	ALPH="QWERTYUIOPASDFGHJKLZXCVBNM"
	for i in s:
		if (i in num) and ("num" not in result):
			result.append("num")
			continue
		elif (i in alph) and ("alph" not in result):
			result.append("alph")
			continue
		elif (i in ALPH) and ("ALPH" not in result):
			result.append("ALPH")
			continue
		elif ("char" not in result):
			result.append("char")
	return result
	

#计算输入字符串中各字符的个数，返回值为数组
def COUNT(s):
	SET=[]
	for i in s:
		if (i not in SET):
			SET.append(i)
	for i in range(len(SET)):
		SET[i]=SET[i]+" : "+str(s.count(SET[i]))
	return SET
	
#提取字符串，第1个参数为原字符串，第2个参数为所需提取的字符串的左边，第3个参数为所需提取的字符串的右边，表达的不是很清楚，自己体会就好了。 (*/ω＼*)
def FIND(str,set1,set2):
	a=str.find(set1)+len(set1)
	b=str.find(set2)
	return str[a:b]	
