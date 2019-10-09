import base64
import base91
import os
import sys
import hashlib
import socket
import re 
sys.setrecursionlimit(1000000)
def B64(s,flg=1):
	if (flg !=0):
		return(base64.b64decode(s))
	else:
		return(base64.b64encode(bytes(s.encode("utf-8"))))
def B32(s,flg=1):
	if (flg !=0):
		return(base64.b32decode(s))
	else:
		return(base64.b32encode(bytes(s.encode("utf-8"))))
def B16(s,flg=1):
	if (flg !=0):
		return(base64.b16decode(s.upper()))
	else:
		return(base64.b16encode(bytes(s.encode("utf-8"))))
def B91(s,flg=1):
	if (flg !=0):
		return(base91.decode(s))
	else:
		return(base91.encode(bytes(s.encode("utf-8"))))
	
	
def CASER(s):
	kslist=list(s)
	for ksn1 in range(26):
		for ksn2 in range(len(s)):
			if "a"<=kslist[ksn2]<="z" or "A"<=kslist[ksn2]<="Z":
				if kslist[ksn2]=="z" or kslist[ksn2]=="Z":
					kslist[ksn2]=chr(ord(kslist[ksn2])-25)
				else:
					kslist[ksn2]=chr(ord(kslist[ksn2])+1)
		kss="".join(kslist)
		print(kss)
	

def REV(s):
	return(''.join(reversed(list(s))))
	
	
def H2B(s):
	temp=bin(eval("0x"+s))[2:]
	for i in range(len(s)*4-len(temp)):
		temp ="0"+temp
	return temp


def B2H(s):
	temp=hex(eval("0b"+s))[2:]
	for i in range(len(s)//4-len(temp)):
		temp ="0"+temp
	return temp
	
	
def FENSE(string,num):
	s=""
	for i in range(num):
		s+=string[i::num]
	return s
	
	
def B2S(s):
	ss=""
	for i in range(len(s)//8):
		ss+=chr(eval("0b"+s[:8]))
		s=s[8:]
	return ss
	
def CLS():
	os.system("cls")
	
	
def NI(a,b):
	for i in range(b):
		if ((1+b*i)%a==0) and ((1+b*i)//a<=b):
			return (1+b*i)//a
			
			
def GCD(a,b):
    if a%b == 0:
        return b
    else :
        return GCD(b,a%b)
		
		
def MD5(s):
	s=bytes(s.encode("utf-8"))
	return hashlib.md5(s).hexdigest()
	
	
def SHA1(s):
	s=bytes(s.encode("utf-8"))
	return hashlib.sha1(s).hexdigest()
	
	
def SHA256(s):
	s=bytes(s.encode("utf-8"))
	return hashlib.sha256(s).hexdigest()
	
	
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
	
	
def COUNT(s):
	SET=[]
	for i in s:
		if (i not in SET):
			SET.append(i)
	for i in range(len(SET)):
		SET[i]=SET[i]+":"+str(s.count(SET[i]))
	return SET
	

def CONNECT(host,port):
	global con
	con=socket.socket()
	con.connect((host,port))
def SEND(message):
	con.send(bytes(message.encode("utf-8"))+b"\n")
def RECV():
	temp=con.recv(1024)
	return temp
	
# class SO:
	# def __init__(self,host,port):
		# host=self.host
		# port=self.port
		# fin=(host,port)
		# con=socket.connect(fin)
	# def SEND(message):
		# con.send(message+"\n")
	# def RECV():
		# temp=con.recv(1024)
		# return temp
		

def FIND(str,set1,set2):
	return str[str.find(set1)+len(set1):str.find(set2)]
	
	
def FREAD(name):
	path="C:\\Users\\Administrator\\Desktop\\"
	f=open(path+name,"r")
	return f.read()
def FWRITE(name,text):
	path="C:\\Users\\Administrator\\Desktop\\"
	f=open(path+name,"w+")
	f.write(text)
	f.close()
	return True
	

def TRY(cmd):
	try:
		eval(cmd)
	except:
		TRY(cmd)

		
def FINDALL(like,str):
	temp=re.compile(like)
	return temp.findall(str)
	
	
def AFFINE(string,b,c):
	sl=[]
	sl2=[]
	b=NI(b,26)
	res=""
	for i in string.lower():
		sl.append(ord(i)-ord("a"))
	for i in sl:
		sl2.append(b*(i-c)%26)
	for i in sl2:
		res+=chr(ord("a")+i)
	return res
