from tkinter import *
from math import *
from ans import *

def fMPlus():
	pass

def fSToD():
	pass

def fENG():
	pass

def fRCL():
	pass

def fHyp():
	pass

def fAngle():
	pass

def fCalc():
	pass

def fOn():
	pass

def fMode():
	pass

def fUp():
	pass

def fDown():
	pass
	
def fLeft():
	global cur, op
	if cur>0:	
		s = ''
		for i in range(cur-1):
			s += str(op[i])
		s += '|'
		for i in range(cur-1, len(op)):
			s += str(op[i])
		tQue.set(s)
		cur -= 1
	return
	
def fRight():
	global cur, op
	if cur<len(op):	
		s = ''
		for i in range(cur+1):
			s += str(op[i])
		s += '|'
		for i in range(cur+1, len(op)):
			s += str(op[i])
		tQue.set(s)
		cur += 1
	return
	
def fShift():
	bUp = Button(frame, bg='#ffffff', command=sfUp, text='')
	bUp.place(x=str(3*w+3.5*s2-w/2)+'c', y=str(d+2*s)+'c', width=str(w)+'c', height=str(2*h/3)+'c')
	bLeft = Button(frame, bg='#ffffff', command=sfLeft, text='')
	bLeft.place(x=str(2*w+3*s2)+'c', y=str(d+2*h/3+2.5*s)+'c', width=str(w)+'c', height=str(2*h/3)+'c')
	bRight = Button(frame, bg='#ffffff', command=sfRight, text='')
	bRight.place(x=str(3*w+4*s2)+'c', y=str(d+2*h/3+2.5*s)+'c', width=str(w)+'c', height=str(2*h/3)+'c')
	bDown = Button(frame, bg='#ffffff', command=sfDown, text='')
	bDown.place(x=str(3*w+3.5*s2-w/2)+'c', y=str(d+4*h/3+3*s)+'c', width=str(w)+'c', height=str(2*h/3)+'c')
	
	bShift = Button(frame, bg='#ffffff', command=sfShift, text='')
	bShift.place(x=str(s2)+'c', y=str(d+2*s)+'c', width=str(w)+'c', height=str(h)+'c')
	bAlpha = Button(frame, bg='#ffffff', command=sfAlpha, text='')
	bAlpha.place(x=str(w+2*s2)+'c', y=str(d+2*s)+'c', width=str(w)+'c', height=str(h)+'c')
	
	bMode = Button(frame, bg='#ffffff', command=sfMode, text='')
	bMode.place(x=str(4*w+5*s2)+'c', y=str(d+2*s)+'c', width=str(w)+'c', height=str(h)+'c')
	bOn = Button(frame, bg='#ffffff', command=sfOn, text='')
	bOn.place(x=str(5*w+6*s2)+'c', y=str(d+2*s)+'c', width=str(w)+'c', height=str(h)+'c')
	
	bCalc = Button(frame, bg='black', command=sfCalc, text='')
	bCalc.place(x=str(s2)+'c', y=str(d+h+3*s)+'c', width=str(w)+'c', height=str(h)+'c')
	bInt = Button(frame, bg='black', command=sfInt, text='')
	bInt.place(x=str(w+2*s2)+'c', y=str(d+h+3*s)+'c', width=str(w)+'c', height=str(h)+'c')
	bInverse = Button(frame, bg='black', command=sfInverse, text='')
	bInverse.place(x=str(4*w+5*s2)+'c', y=str(d+h+3*s)+'c', width=str(w)+'c', height=str(h)+'c')
	bLog = Button(frame, bg='black', command=sfLog, text='=')
	bLog.place(x=str(5*w+6*s2)+'c', y=str(d+h+3*s)+'c', width=str(w)+'c', height=str(h)+'c')
	
	bRatio = Button(frame, bg='black', command=sfRatio, text='') 
	bRatio.place(x=str(s2)+'c', y=str(d+2*h+4*s)+'c', width=str(w)+'c', height=str(h)+'c')
	bRoot = Button(frame, bg='black', command=sfRoot, text='')
	bRoot.place(x=str(w+2*s2)+'c', y=str(d+2*h+4*s)+'c', width=str(w)+'c', height=str(h)+'c')
	bSquare = Button(frame, bg='black', command=sfSquare, text='')
	bSquare.place(x=str(2*w+3*s2)+'c', y=str(d+2*h+4*s)+'c', width=str(w)+'c', height=str(h)+'c')
	bPower = Button(frame, bg='black', command=sfPower, text='')
	bPower.place(x=str(3*w+4*s2)+'c', y=str(d+2*h+4*s)+'c', width=str(w)+'c', height=str(h)+'c')
	bLog10 = Button(frame, bg='black', command=sfLog10, text='')
	bLog10.place(x=str(4*w+5*s2)+'c', y=str(d+2*h+4*s)+'c', width=str(w)+'c', height=str(h)+'c')
	bLogE = Button(frame, bg='black', command=sfLogE, text='')
	bLogE.place(x=str(5*w+6*s2)+'c', y=str(d+2*h+4*s)+'c', width=str(w)+'c', height=str(h)+'c')
	
	bMinus = Button(frame, bg='black', command=sfMinus, fg='blue', text='A')
	bMinus.place(x=str(s2)+'c', y=str(d+3*h+5*s)+'c', width=str(w)+'c', height=str(h)+'c')
	bAngle = Button(frame, bg='black', command=sfAngle, fg='blue', text='B')
	bAngle.place(x=str(w+2*s2)+'c', y=str(d+3*h+5*s)+'c', width=str(w)+'c', height=str(h)+'c')
	bHyp = Button(frame, bg='black', command=sfHyp, fg='blue', text='C')
	bHyp.place(x=str(2*w+3*s2)+'c', y=str(d+3*h+5*s)+'c', width=str(w)+'c', height=str(h)+'c')
	bSin = Button(frame, bg='black', command=sfSin, fg='blue', text='D')
	bSin.place(x=str(3*w+4*s2)+'c', y=str(d+3*h+5*s)+'c', width=str(w)+'c', height=str(h)+'c')
	bCos = Button(frame, bg='black', command=sfCos, fg='blue', text='E')
	bCos.place(x=str(4*w+5*s2)+'c', y=str(d+3*h+5*s)+'c', width=str(w)+'c', height=str(h)+'c')
	bTan = Button(frame, bg='black', command=sfTan, fg='blue', text='F')
	bTan.place(x=str(5*w+6*s2)+'c', y=str(d+3*h+5*s)+'c', width=str(w)+'c', height=str(h)+'c')
	
	bRCL = Button(frame, bg='black', command=sfRCL, text='')
	bRCL.place(x=str(s2)+'c', y=str(d+4*h+6*s)+'c', width=str(w)+'c', height=str(h)+'c')
	bENG = Button(frame, bg='black', command=sfENG, text='')
	bENG.place(x=str(w+2*s2)+'c', y=str(d+4*h+6*s)+'c', width=str(w)+'c', height=str(h)+'c')
	bBracketL = Button(frame, bg='black', command=sfBracketL, text='')
	bBracketL.place(x=str(2*w+3*s2)+'c', y=str(d+4*h+6*s)+'c', width=str(w)+'c', height=str(h)+'c')
	bBracketR = Button(frame, bg='black', command=sfBracketR, fg='blue', text='')
	bBracketR.place(x=str(3*w+4*s2)+'c', y=str(d+4*h+6*s)+'c', width=str(w)+'c', height=str(h)+'c')
	bSToD = Button(frame, bg='black', command=sfSToD, fg='blue', text='')
	bSToD.place(x=str(4*w+5*s2)+'c', y=str(d+4*h+6*s)+'c', width=str(w)+'c', height=str(h)+'c')
	bMPlus = Button(frame, bg='black', command=sfMPlus, fg='blue', text='')
	bMPlus.place(x=str(5*w+6*s2)+'c', y=str(d+4*h+6*s)+'c', width=str(w)+'c', height=str(h)+'c')
	
	b7 = Button(frame, bg='#ffffff', command=sf7, text='')
	b7.place(x=str(s1)+'c', y=str(d+5*h+7*s)+'c', width=str(w)+'c', height=str(h)+'c')
	b8 = Button(frame, bg='#ffffff', command=sf8, text='')
	b8.place(x=str(w+2*s1)+'c', y=str(d+5*h+7*s)+'c', width=str(w)+'c', height=str(h)+'c')
	b9 = Button(frame, bg='#ffffff', command=sf9, text='')
	b9.place(x=str(2*w+3*s1)+'c', y=str(d+5*h+7*s)+'c', width=str(w)+'c', height=str(h)+'c')
	bDel = Button(frame, bg='orange', command=sfDel, text='')
	bDel.place(x=str(3*w+4*s1)+'c', y=str(d+5*h+7*s)+'c', width=str(w)+'c', height=str(h)+'c')
	bAC = Button(frame, bg='orange', command=sfAC, text='')
	bAC.place(x=str(4*w+5*s1)+'c', y=str(d+5*h+7*s)+'c', width=str(w)+'c', height=str(h)+'c')
	
	b4 = Button(frame, bg='#ffffff', command=sf4, text='')
	b4.place(x=str(s1)+'c', y=str(d+6*h+8*s)+'c', width=str(w)+'c', height=str(h)+'c')
	b5 = Button(frame, bg='#ffffff', command=sf5, text='')
	b5.place(x=str(w+2*s1)+'c', y=str(d+6*h+8*s)+'c', width=str(w)+'c', height=str(h)+'c')
	b6 = Button(frame, bg='#ffffff', command=sf6, text='')
	b6.place(x=str(2*w+3*s1)+'c', y=str(d+6*h+8*s)+'c', width=str(w)+'c', height=str(h)+'c')
	bMul = Button(frame, bg='#ffffff', command=sfMul, text='')
	bMul.place(x=str(3*w+4*s1)+'c', y=str(d+6*h+8*s)+'c', width=str(w)+'c', height=str(h)+'c')
	bDiv = Button(frame, bg='#ffffff', command=sfDiv, text='')
	bDiv.place(x=str(4*w+5*s1)+'c', y=str(d+6*h+8*s)+'c', width=str(w)+'c', height=str(h)+'c')
	
	b1 = Button(frame, bg='#ffffff', command=sf1, text='')
	b1.place(x=str(s1)+'c', y=str(d+7*h+9*s)+'c', width=str(w)+'c', height=str(h)+'c')
	b2 = Button(frame, bg='#ffffff', command=sf2, text='')
	b2.place(x=str(w+2*s1)+'c', y=str(d+7*h+9*s)+'c', width=str(w)+'c', height=str(h)+'c')
	b3 = Button(frame, bg='#ffffff', command=sf3, text='')
	b3.place(x=str(2*w+3*s1)+'c', y=str(d+7*h+9*s)+'c', width=str(w)+'c', height=str(h)+'c')
	bPlus = Button(frame, bg='#ffffff', command=sfPlus, text='')
	bPlus.place(x=str(3*w+4*s1)+'c', y=str(d+7*h+9*s)+'c', width=str(w)+'c', height=str(h)+'c')
	bSub = Button(frame, bg='#ffffff', command=sfSub, text='')
	bSub.place(x=str(4*w+5*s1)+'c', y=str(d+7*h+9*s)+'c', width=str(w)+'c', height=str(h)+'c')
	
	b0 = Button(frame, bg='#ffffff', command=sf0,text='')
	b0.place(x=str(s1)+'c', y=str(d+8*h+10*s)+'c', width=str(w)+'c', height=str(h)+'c')
	bDot = Button(frame, bg='#ffffff', command=sfDot, text='')
	bDot.place(x=str(w+2*s1)+'c', y=str(d+8*h+10*s)+'c', width=str(w)+'c', height=str(h)+'c')
	b10X = Button(frame, bg='#ffffff', fg='blue', command=sf10X, text='')
	b10X.place(x=str(2*w+3*s1)+'c', y=str(d+8*h+10*s)+'c', width=str(w)+'c', height=str(h)+'c')
	bAns = Button(frame, bg='#ffffff', command=sfAns, text='')
	bAns.place(x=str(3*w+4*s1)+'c', y=str(d+8*h+10*s)+'c', width=str(w)+'c', height=str(h)+'c')
	bEqual = Button(frame, bg='#ffffff', command=sfEqual, text='')
	bEqual.place(x=str(4*w+5*s1)+'c', y=str(d+8*h+10*s)+'c', width=str(w)+'c', height=str(h)+'c')
	return
	
def fAlpha():
	bUp = Button(frame, bg='#ffffff', command=afUp, text='')
	bUp.place(x=str(3*w+3.5*s2-w/2)+'c', y=str(d+2*s)+'c', width=str(w)+'c', height=str(2*h/3)+'c')
	bLeft = Button(frame, bg='#ffffff', command=afLeft, text='')
	bLeft.place(x=str(2*w+3*s2)+'c', y=str(d+2*h/3+2.5*s)+'c', width=str(w)+'c', height=str(2*h/3)+'c')
	bRight = Button(frame, bg='#ffffff', command=afRight, text='')
	bRight.place(x=str(3*w+4*s2)+'c', y=str(d+2*h/3+2.5*s)+'c', width=str(w)+'c', height=str(2*h/3)+'c')
	bDown = Button(frame, bg='#ffffff', command=afDown, text='')
	bDown.place(x=str(3*w+3.5*s2-w/2)+'c', y=str(d+4*h/3+3*s)+'c', width=str(w)+'c', height=str(2*h/3)+'c')
	
	bShift = Button(frame, bg='#ffffff', command=afShift, text='')
	bShift.place(x=str(s2)+'c', y=str(d+2*s)+'c', width=str(w)+'c', height=str(h)+'c')
	bAlpha = Button(frame, bg='#ffffff', command=afAlpha, text='')
	bAlpha.place(x=str(w+2*s2)+'c', y=str(d+2*s)+'c', width=str(w)+'c', height=str(h)+'c')
	
	bMode = Button(frame, bg='#ffffff', command=afMode, text='')
	bMode.place(x=str(4*w+5*s2)+'c', y=str(d+2*s)+'c', width=str(w)+'c', height=str(h)+'c')
	bOn = Button(frame, bg='#ffffff', command=afOn, text='')
	bOn.place(x=str(5*w+6*s2)+'c', y=str(d+2*s)+'c', width=str(w)+'c', height=str(h)+'c')
	
	bCalc = Button(frame, bg='black', command=afCalc, text='')
	bCalc.place(x=str(s2)+'c', y=str(d+h+3*s)+'c', width=str(w)+'c', height=str(h)+'c')
	bInt = Button(frame, bg='black', command=afInt, text='')
	bInt.place(x=str(w+2*s2)+'c', y=str(d+h+3*s)+'c', width=str(w)+'c', height=str(h)+'c')
	bInverse = Button(frame, bg='black', command=afInverse, text='')
	bInverse.place(x=str(4*w+5*s2)+'c', y=str(d+h+3*s)+'c', width=str(w)+'c', height=str(h)+'c')
	bLog = Button(frame, bg='black', command=afLog, text='=')
	bLog.place(x=str(5*w+6*s2)+'c', y=str(d+h+3*s)+'c', width=str(w)+'c', height=str(h)+'c')
	
	bRatio = Button(frame, bg='black', command=afRatio, text='') 
	bRatio.place(x=str(s2)+'c', y=str(d+2*h+4*s)+'c', width=str(w)+'c', height=str(h)+'c')
	bRoot = Button(frame, bg='black', command=afRoot, text='')
	bRoot.place(x=str(w+2*s2)+'c', y=str(d+2*h+4*s)+'c', width=str(w)+'c', height=str(h)+'c')
	bSquare = Button(frame, bg='black', command=afSquare, text='')
	bSquare.place(x=str(2*w+3*s2)+'c', y=str(d+2*h+4*s)+'c', width=str(w)+'c', height=str(h)+'c')
	bPower = Button(frame, bg='black', command=afPower, text='')
	bPower.place(x=str(3*w+4*s2)+'c', y=str(d+2*h+4*s)+'c', width=str(w)+'c', height=str(h)+'c')
	bLog10 = Button(frame, bg='black', command=afLog10, text='')
	bLog10.place(x=str(4*w+5*s2)+'c', y=str(d+2*h+4*s)+'c', width=str(w)+'c', height=str(h)+'c')
	bLogE = Button(frame, bg='black', command=afLogE, text='')
	bLogE.place(x=str(5*w+6*s2)+'c', y=str(d+2*h+4*s)+'c', width=str(w)+'c', height=str(h)+'c')
	
	bMinus = Button(frame, bg='black', command=afMinus, fg='red', text='A')
	bMinus.place(x=str(s2)+'c', y=str(d+3*h+5*s)+'c', width=str(w)+'c', height=str(h)+'c')
	bAngle = Button(frame, bg='black', command=afAngle, fg='red', text='B')
	bAngle.place(x=str(w+2*s2)+'c', y=str(d+3*h+5*s)+'c', width=str(w)+'c', height=str(h)+'c')
	bHyp = Button(frame, bg='black', command=afHyp, fg='red', text='C')
	bHyp.place(x=str(2*w+3*s2)+'c', y=str(d+3*h+5*s)+'c', width=str(w)+'c', height=str(h)+'c')
	bSin = Button(frame, bg='black', command=afSin, fg='red', text='D')
	bSin.place(x=str(3*w+4*s2)+'c', y=str(d+3*h+5*s)+'c', width=str(w)+'c', height=str(h)+'c')
	bCos = Button(frame, bg='black', command=afCos, fg='red', text='E')
	bCos.place(x=str(4*w+5*s2)+'c', y=str(d+3*h+5*s)+'c', width=str(w)+'c', height=str(h)+'c')
	bTan = Button(frame, bg='black', command=afTan, fg='red', text='F')
	bTan.place(x=str(5*w+6*s2)+'c', y=str(d+3*h+5*s)+'c', width=str(w)+'c', height=str(h)+'c')
	
	bRCL = Button(frame, bg='black', command=afRCL, text='')
	bRCL.place(x=str(s2)+'c', y=str(d+4*h+6*s)+'c', width=str(w)+'c', height=str(h)+'c')
	bENG = Button(frame, bg='black', command=afENG, text='')
	bENG.place(x=str(w+2*s2)+'c', y=str(d+4*h+6*s)+'c', width=str(w)+'c', height=str(h)+'c')
	bBracketL = Button(frame, bg='black', command=afBracketL, text='')
	bBracketL.place(x=str(2*w+3*s2)+'c', y=str(d+4*h+6*s)+'c', width=str(w)+'c', height=str(h)+'c')
	bBracketR = Button(frame, bg='black', command=afBracketR, fg='red', text='X')
	bBracketR.place(x=str(3*w+4*s2)+'c', y=str(d+4*h+6*s)+'c', width=str(w)+'c', height=str(h)+'c')
	bSToD = Button(frame, bg='black', command=afSToD, fg='red', text='Y')
	bSToD.place(x=str(4*w+5*s2)+'c', y=str(d+4*h+6*s)+'c', width=str(w)+'c', height=str(h)+'c')
	bMPlus = Button(frame, bg='black', command=afMPlus, fg='red', text='M')
	bMPlus.place(x=str(5*w+6*s2)+'c', y=str(d+4*h+6*s)+'c', width=str(w)+'c', height=str(h)+'c')
	
	b7 = Button(frame, bg='#ffffff', command=af7, text='')
	b7.place(x=str(s1)+'c', y=str(d+5*h+7*s)+'c', width=str(w)+'c', height=str(h)+'c')
	b8 = Button(frame, bg='#ffffff', command=af8, text='')
	b8.place(x=str(w+2*s1)+'c', y=str(d+5*h+7*s)+'c', width=str(w)+'c', height=str(h)+'c')
	b9 = Button(frame, bg='#ffffff', command=af9, text='')
	b9.place(x=str(2*w+3*s1)+'c', y=str(d+5*h+7*s)+'c', width=str(w)+'c', height=str(h)+'c')
	bDel = Button(frame, bg='orange', command=afDel, text='')
	bDel.place(x=str(3*w+4*s1)+'c', y=str(d+5*h+7*s)+'c', width=str(w)+'c', height=str(h)+'c')
	bAC = Button(frame, bg='orange', command=afAC, text='')
	bAC.place(x=str(4*w+5*s1)+'c', y=str(d+5*h+7*s)+'c', width=str(w)+'c', height=str(h)+'c')
	
	b4 = Button(frame, bg='#ffffff', command=af4, text='')
	b4.place(x=str(s1)+'c', y=str(d+6*h+8*s)+'c', width=str(w)+'c', height=str(h)+'c')
	b5 = Button(frame, bg='#ffffff', command=af5, text='')
	b5.place(x=str(w+2*s1)+'c', y=str(d+6*h+8*s)+'c', width=str(w)+'c', height=str(h)+'c')
	b6 = Button(frame, bg='#ffffff', command=af6, text='')
	b6.place(x=str(2*w+3*s1)+'c', y=str(d+6*h+8*s)+'c', width=str(w)+'c', height=str(h)+'c')
	bMul = Button(frame, bg='#ffffff', command=afMul, text='')
	bMul.place(x=str(3*w+4*s1)+'c', y=str(d+6*h+8*s)+'c', width=str(w)+'c', height=str(h)+'c')
	bDiv = Button(frame, bg='#ffffff', command=afDiv, text='')
	bDiv.place(x=str(4*w+5*s1)+'c', y=str(d+6*h+8*s)+'c', width=str(w)+'c', height=str(h)+'c')
	
	b1 = Button(frame, bg='#ffffff', command=af1, text='')
	b1.place(x=str(s1)+'c', y=str(d+7*h+9*s)+'c', width=str(w)+'c', height=str(h)+'c')
	b2 = Button(frame, bg='#ffffff', command=af2, text='')
	b2.place(x=str(w+2*s1)+'c', y=str(d+7*h+9*s)+'c', width=str(w)+'c', height=str(h)+'c')
	b3 = Button(frame, bg='#ffffff', command=af3, text='')
	b3.place(x=str(2*w+3*s1)+'c', y=str(d+7*h+9*s)+'c', width=str(w)+'c', height=str(h)+'c')
	bPlus = Button(frame, bg='#ffffff', command=afPlus, text='')
	bPlus.place(x=str(3*w+4*s1)+'c', y=str(d+7*h+9*s)+'c', width=str(w)+'c', height=str(h)+'c')
	bSub = Button(frame, bg='#ffffff', command=afSub, text='')
	bSub.place(x=str(4*w+5*s1)+'c', y=str(d+7*h+9*s)+'c', width=str(w)+'c', height=str(h)+'c')
	
	b0 = Button(frame, bg='#ffffff', command=af0,text='')
	b0.place(x=str(s1)+'c', y=str(d+8*h+10*s)+'c', width=str(w)+'c', height=str(h)+'c')
	bDot = Button(frame, bg='#ffffff', command=afDot, text='')
	bDot.place(x=str(w+2*s1)+'c', y=str(d+8*h+10*s)+'c', width=str(w)+'c', height=str(h)+'c')
	b10X = Button(frame, bg='#ffffff', fg='red', command=af10X, text='e')
	b10X.place(x=str(2*w+3*s1)+'c', y=str(d+8*h+10*s)+'c', width=str(w)+'c', height=str(h)+'c')
	bAns = Button(frame, bg='#ffffff', command=afAns, text='')
	bAns.place(x=str(3*w+4*s1)+'c', y=str(d+8*h+10*s)+'c', width=str(w)+'c', height=str(h)+'c')
	bEqual = Button(frame, bg='#ffffff', command=afEqual, text='')
	bEqual.place(x=str(4*w+5*s1)+'c', y=str(d+8*h+10*s)+'c', width=str(w)+'c', height=str(h)+'c')
	return
	
def fInt():
	global cur, op
	s = ''
	for i in range(cur):
		s += str(op[i])
	s += chr(643) + '_(|)^()()dx'
	for i in range(cur, len(op)):
		s += str(op[i])
	tQue.set(s)
	op = op[:cur] + [chr(643)+'_('] + op[cur:]
	op = op[:cur+1] + [')^('] + op[cur+1:]
	op = op[:cur+2] + [')('] + op[cur+2:]
	op = op[:cur+3] + [')dx'] + op[cur+3:]
	cur += 1
	return

def fInverse():
	
	return
	
def fLog():
	global cur, op
	s = ''
	for i in range(cur):
		s += str(op[i])
	s += 'log_(|)()'
	for i in range(cur, len(op)):
		s += str(op[i])
	tQue.set(s)
	op = op[:cur] + ['log_('] + op[cur:]
	op = op[:cur+1] + [')('] + op[cur+1:]
	op = op[:cur+2] + [')'] + op[cur+2:]
	cur += 1
	return

def fRatio():
	global cur, op
	s = ''
	for i in range(cur):
		s += str(op[i])
	s += '(|)/()'
	for i in range(cur, len(op)):
		s += str(op[i])
	tQue.set(s)
	op = op[:cur] + ['('] + op[cur:]
	op = op[:cur+1] + [')/('] + op[cur+1:]
	op = op[:cur+2] + [')'] + op[cur+2:]
	cur += 1
	return

def fRoot():
	global cur, op
	s = ''
	for i in range(cur):
		s += str(op[i])
	s += chr(8730) + '(|)'
	for i in range(cur, len(op)):
		s += str(op[i])
	tQue.set(s)
	op = op[:cur] + [chr(8730) + '('] + op[cur:]
	op = op[:cur+1] + [')'] + op[cur+1:]
	cur += 1
	return

def fSquare():
	global cur, op
	s = ''
	for i in range(cur):
		s += str(op[i])
	s += '^2|'
	for i in range(cur, len(op)):
		s += str(op[i])
	tQue.set(s)
	op = op[:cur] + ['^2'] + op[cur:]
	cur += 1
	return

def fPower():
	global cur, op
	s = ''
	for i in range(cur):
		s += str(op[i])
	s += '^(|)'
	for i in range(cur, len(op)):
		s += str(op[i])
	tQue.set(s)
	op = op[:cur] + ['^('] + op[cur:]
	op = op[:cur+1] + [')'] + op[cur+1:]
	cur += 1
	return

def fLog10():
	global cur, op
	s = ''
	for i in range(cur):
		s += str(op[i])
	s += 'log(|)'
	for i in range(cur, len(op)):
		s += str(op[i])
	tQue.set(s)
	op = op[:cur] + ['log('] + op[cur:]
	op = op[:cur+1] + [')'] + op[cur+1:]
	cur += 1
	return

def fLogE():
	global cur, op
	s = ''
	for i in range(cur):
		s += str(op[i])
	s += 'ln(|)'
	for i in range(cur, len(op)):
		s += str(op[i])
	tQue.set(s)
	op = op[:cur] + ['ln('] + op[cur:]
	op = op[:cur+1] + [')'] + op[cur+1:]
	cur += 1
	return

def fMinus():
	global cur, op
	s = ''
	for i in range(cur):
		s += str(op[i])
	s += '-|'
	for i in range(cur, len(op)):
		s += str(op[i])
	tQue.set(s)
	op = op[:cur] + ['-'] + op[cur:]
	cur += 1
	return
	
def afMinus():
	global cur, op
	s = ''
	for i in range(cur):
		s += str(op[i])
	s += 'A|'
	for i in range(cur, len(op)):
		s += str(op[i])
	tQue.set(s)
	op = op[:cur] + ['A'] + op[cur:]
	cur += 1
	init()
	return

def afAngle():
	global cur, op
	s = ''
	for i in range(cur):
		s += str(op[i])
	s += 'B|'
	for i in range(cur, len(op)):
		s += str(op[i])
	tQue.set(s)
	op = op[:cur] + ['B'] + op[cur:]
	cur += 1
	init()
	return

def afHyp():
	global cur, op
	s = ''
	for i in range(cur):
		s += str(op[i])
	s += 'C|'
	for i in range(cur, len(op)):
		s += str(op[i])
	tQue.set(s)
	op = op[:cur] + ['C'] + op[cur:]
	cur += 1
	init()
	return

def fSin():
	global cur, op
	s = ''
	for i in range(cur):
		s += str(op[i])
	s += 'sin(|)'
	for i in range(cur, len(op)):
		s += str(op[i])
	tQue.set(s)
	op = op[:cur] + ['sin('] + op[cur:]
	op = op[:cur+1] + [')'] + op[cur+1:]
	cur += 1
	return
	
def afSin():
	global cur, op
	s = ''
	for i in range(cur):
		s += str(op[i])
	s += 'D|'
	for i in range(cur, len(op)):
		s += str(op[i])
	tQue.set(s)
	op = op[:cur] + ['D'] + op[cur:]
	cur += 1
	init()
	return

def fCos():
	global cur, op
	s = ''
	for i in range(cur):
		s += str(op[i])
	s += 'cos(|)'
	for i in range(cur, len(op)):
		s += str(op[i])
	tQue.set(s)
	op = op[:cur] + ['cos('] + op[cur:]
	op = op[:cur+1] + [')'] + op[cur+1:]
	cur += 1
	return

def afCos():
	global cur, op
	s = ''
	for i in range(cur):
		s += str(op[i])
	s += 'E|'
	for i in range(cur, len(op)):
		s += str(op[i])
	tQue.set(s)
	op = op[:cur] + ['E'] + op[cur:]
	cur += 1
	init()
	return

def fTan():
	global cur, op
	s = ''
	for i in range(cur):
		s += str(op[i])
	s += 'tan(|)'
	for i in range(cur, len(op)):
		s += str(op[i])
	tQue.set(s)
	op = op[:cur] + ['tan('] + op[cur:]
	op = op[:cur+1] + [')'] + op[cur+1:]
	cur += 1
	return

def afTan():
	global cur, op
	s = ''
	for i in range(cur):
		s += str(op[i])
	s += 'F|'
	for i in range(cur, len(op)):
		s += str(op[i])
	tQue.set(s)
	op = op[:cur] + ['F'] + op[cur:]
	cur += 1
	init()
	return

def fBracketL():
	global cur, op
	s = ''
	for i in range(cur):
		s += str(op[i])
	s += '(|'
	for i in range(cur, len(op)):
		s += str(op[i])
	tQue.set(s)
	op = op[:cur] + ['('] + op[cur:]
	cur += 1
	return

def fBracketR():
	global cur, op
	s = ''
	for i in range(cur):
		s += str(op[i])
	s += ')|'
	for i in range(cur, len(op)):
		s += str(op[i])
	tQue.set(s)
	op = op[:cur] + [')'] + op[cur:]
	cur += 1
	return
	
def afBracketR():
	global cur, op
	s = ''
	for i in range(cur):
		s += str(op[i])
	s += 'X|'
	for i in range(cur, len(op)):
		s += str(op[i])
	tQue.set(s)
	op = op[:cur] + ['X'] + op[cur:]
	cur += 1
	init()
	return

def afSToD():
	global cur, op
	s = ''
	for i in range(cur):
		s += str(op[i])
	s += 'Y|'
	for i in range(cur, len(op)):
		s += str(op[i])
	tQue.set(s)
	op = op[:cur] + ['Y'] + op[cur:]
	cur += 1
	init()
	return

def afMPlus():
	global cur, op
	s = ''
	for i in range(cur):
		s += str(op[i])
	s += 'M|'
	for i in range(cur, len(op)):
		s += str(op[i])
	tQue.set(s)
	op = op[:cur] + ['M'] + op[cur:]
	cur += 1
	init()
	return

def f7():
	global cur, op
	s = ''
	for i in range(cur):
		s += str(op[i])
	s += '7|'
	for i in range(cur, len(op)):
		s += str(op[i])
	tQue.set(s)
	op = op[:cur] + ['7'] + op[cur:]
	cur += 1
	return

def f8():
	global cur, op
	s = ''
	for i in range(cur):
		s += str(op[i])
	s += '8|'
	for i in range(cur, len(op)):
		s += str(op[i])
	tQue.set(s)
	op = op[:cur] + ['8'] + op[cur:]
	cur += 1
	return

def f9():
	global cur, op
	s = ''
	for i in range(cur):
		s += str(op[i])
	s += '9|'
	for i in range(cur, len(op)):
		s += str(op[i])
	tQue.set(s)
	op = op[:cur] + ['9'] + op[cur:]
	cur += 1
	return

def fDel():
	global cur, op
	if len(op) > 0:
		del op[cur-1]
		cur -= 1
		s = ''
		for i in range(cur):
			s += op[i]
		s += '|'
		for i in range(cur,len(op)):
			s += op[i]
		tQue.set(s)
	return

def fAC():
	global cur, op
	tQue.set('')
	tAns.set('')
	op = []
	cur = 0
	return

def f4():
	global cur, op
	s = ''
	for i in range(cur):
		s += str(op[i])
	s += '4|'
	for i in range(cur, len(op)):
		s += str(op[i])
	tQue.set(s)
	op = op[:cur] + ['4'] + op[cur:]
	cur += 1
	return

def f5():
	global cur, op
	s = ''
	for i in range(cur):
		s += str(op[i])
	s += '5|'
	for i in range(cur, len(op)):
		s += str(op[i])
	tQue.set(s)
	op = op[:cur] + ['5'] + op[cur:]
	cur += 1
	return

def f6():
	global cur, op
	s = ''
	for i in range(cur):
		s += str(op[i])
	s += '6|'
	for i in range(cur, len(op)):
		s += str(op[i])
	tQue.set(s)
	op = op[:cur] + ['6'] + op[cur:]
	cur += 1
	return

def fMul():
	global cur, op
	s = ''
	for i in range(cur):
		s += str(op[i])
	s += chr(735)
	for i in range(cur, len(op)):
		s += str(op[i])
	tQue.set(s)
	op = op[:cur] + [chr(735)] + op[cur:]
	cur += 1
	return

def fDiv():
	global cur, op
	s = ''
	for i in range(cur):
		s += str(op[i])
	s += chr(247)
	for i in range(cur, len(op)):
		s += str(op[i])
	tQue.set(s)
	op = op[:cur] + [chr(247)] + op[cur:]
	cur += 1
	return

def f1():
	global cur, op
	s = ''
	for i in range(cur):
		s += str(op[i])
	s += '1|'
	for i in range(cur, len(op)):
		s += str(op[i])
	tQue.set(s)
	op = op[:cur] + ['1'] + op[cur:]
	cur += 1
	return

def f2():
	global cur, op
	s = ''
	for i in range(cur):
		s += str(op[i])
	s += '2|'
	for i in range(cur, len(op)):
		s += str(op[i])
	tQue.set(s)
	op = op[:cur] + ['2'] + op[cur:]
	cur += 1
	return

def f3():
	global cur, op
	s = ''
	for i in range(cur):
		s += str(op[i])
	s += '3|'
	for i in range(cur, len(op)):
		s += str(op[i])
	tQue.set(s)
	op = op[:cur] + ['3'] + op[cur:]
	cur += 1
	return

def fPlus():
	global cur, op
	s = ''
	for i in range(cur):
		s += str(op[i])
	s += '+|'
	for i in range(cur, len(op)):
		s += str(op[i])
	tQue.set(s)
	op = op[:cur] + ['+'] + op[cur:]
	cur += 1
	return

def fSub():
	global cur, op
	s = ''
	for i in range(cur):
		s += str(op[i])
	s += '-|'
	for i in range(cur, len(op)):
		s += str(op[i])
	tQue.set(s)
	op = op[:cur] + ['-'] + op[cur:]
	cur += 1
	return

def f0():
	global cur, op
	s = ''
	for i in range(cur):
		s += str(op[i])
	s += '0|'
	for i in range(cur, len(op)):
		s += str(op[i])
	tQue.set(s)
	op = op[:cur] + ['0'] + op[cur:]
	cur += 1
	return

def fDot():
	global cur, op
	s = ''
	for i in range(cur):
		s += str(op[i])
	s += '.|'
	for i in range(cur, len(op)):
		s += str(op[i])
	tQue.set(s)
	op = op[:cur] + ['.'] + op[cur:]
	cur += 1
	return

def f10X():
	global cur, op
	s = ''
	for i in range(cur):
		s += str(op[i])
	s += chr(735)+'10^|'
	for i in range(cur, len(op)):
		s += str(op[i])
	tQue.set(s)
	op = op[:cur] + [chr(735)+'10^'] + op[cur:]
	cur += 1
	return
	
def af10X():
	global cur, op
	s = ''
	for i in range(cur):
		s += str(op[i])
	s += 'e|'
	for i in range(cur, len(op)):
		s += str(op[i])
	tQue.set(s)
	op = op[:cur] + ['e'] + op[cur:]
	cur += 1
	init()
	return

def fAns():
	global cur, op
	s = ''
	for i in range(cur):
		s += str(op[i])
	s += 'Ans|'
	for i in range(cur, len(op)):
		s += str(op[i])
	tQue.set(s)
	op = op[:cur] + ['Ans'] + op[cur:]
	cur += 1
	return

def fEqual():
	global op, Ans, ansMode
	ansMode = True
	s = ''
	for i in op:
		s += i
	s = s.replace(chr(735),'*')
	s = s.replace(chr(247),'/')
	s = s.replace('^','**')
	s = logarithm(s)
	s = s.replace('log', 'log10')
	s = s.replace('ln', 'log')
	s = root(s)
	s = integral(s)
	s = s.replace('Ans',str(Ans))
	s = s.replace('A',str(A))
	s = s.replace('B',str(B))
	s = s.replace('C',str(C))
	s = s.replace('D',str(D))
	s = s.replace('E',str(E))
	s = s.replace('F',str(F))
	s = s.replace('X',str(X))
	s = s.replace('Y',str(Y))
	s = s.replace('M',str(M))
	s = s.replace('e',str(exp(1)))
	print(s)
	try:
		Ans = eval(s)
		tAns.set(str(Ans))
	except SyntaxError:
		tAns.set('Syntax Error')
	return

def init():
	displayFrame = Frame(frame, bg='#00ff00')
	displayFrame.place(x=str(s1)+'c', y=str(s)+'c', width=str(5*w+4*s1)+'c', height=str(d)+'c')
	lQue = Label(displayFrame, anchor='w', bg='#00ff00', textvariable=tQue)
	lQue.place(x=str(s1)+'c', y=str(s)+'c', width=str(5*w+2*s1)+'c', height=str(d/2-s)+'c')
	lAns = Label(displayFrame, anchor='e', bg='#00ff00', textvariable=tAns)
	lAns.place(x=str(s1)+'c', y=str(d/2)+'c', width=str(5*w+2*s1)+'c', height=str(d/2-s)+'c')
	
	bUp = Button(frame, bg='#ffffff', command=fUp, text=chr(708))
	bUp.place(x=str(3*w+3.5*s2-w/2)+'c', y=str(d+2*s)+'c', width=str(w)+'c', height=str(2*h/3)+'c')
	bLeft = Button(frame, bg='#ffffff', command=fLeft, text=chr(706))
	bLeft.place(x=str(2*w+3*s2)+'c', y=str(d+2*h/3+2.5*s)+'c', width=str(w)+'c', height=str(2*h/3)+'c')
	bRight = Button(frame, bg='#ffffff', command=fRight, text=chr(707))
	bRight.place(x=str(3*w+4*s2)+'c', y=str(d+2*h/3+2.5*s)+'c', width=str(w)+'c', height=str(2*h/3)+'c')
	bDown = Button(frame, bg='#ffffff', command=fDown, text=chr(709))
	bDown.place(x=str(3*w+3.5*s2-w/2)+'c', y=str(d+4*h/3+3*s)+'c', width=str(w)+'c', height=str(2*h/3)+'c')
	
	bShift = Button(frame, bg='#ffffff', command=fShift, fg='blue', text='Shift')
	bShift.place(x=str(s2)+'c', y=str(d+2*s)+'c', width=str(w)+'c', height=str(h)+'c')
	bAlpha = Button(frame, bg='#ffffff', command=fAlpha, fg='red', text='Alpha')
	bAlpha.place(x=str(w+2*s2)+'c', y=str(d+2*s)+'c', width=str(w)+'c', height=str(h)+'c')
	
	bMode = Button(frame, bg='#ffffff', command=fMode, text='Mode')
	bMode.place(x=str(4*w+5*s2)+'c', y=str(d+2*s)+'c', width=str(w)+'c', height=str(h)+'c')
	bOn = Button(frame, bg='#ffffff', command=fOn, text='On')
	bOn.place(x=str(5*w+6*s2)+'c', y=str(d+2*s)+'c', width=str(w)+'c', height=str(h)+'c')
	
	bCalc = Button(frame, bg='black', command=fCalc, fg='#ffffff', text='Calc')
	bCalc.place(x=str(s2)+'c', y=str(d+h+3*s)+'c', width=str(w)+'c', height=str(h)+'c')
	bInt = Button(frame, bg='black', command=fInt, fg='#ffffff', text=chr(643))
	bInt.place(x=str(w+2*s2)+'c', y=str(d+h+3*s)+'c', width=str(w)+'c', height=str(h)+'c')
	bInverse = Button(frame, bg='black', command=fInverse, fg='#ffffff', text='x^-1')
	bInverse.place(x=str(4*w+5*s2)+'c', y=str(d+h+3*s)+'c', width=str(w)+'c', height=str(h)+'c')
	bLog = Button(frame, bg='black', command=fLog, fg='#ffffff', text='log_'+chr(9633))
	bLog.place(x=str(5*w+6*s2)+'c', y=str(d+h+3*s)+'c', width=str(w)+'c', height=str(h)+'c')
	
	bRatio = Button(frame, bg='black', command=fRatio, fg='#ffffff', text=chr(9633)+'/'+chr(9633)) 
	bRatio.place(x=str(s2)+'c', y=str(d+2*h+4*s)+'c', width=str(w)+'c', height=str(h)+'c')
	bRoot = Button(frame, bg='black', command=fRoot, fg='#ffffff', text=chr(8730))
	bRoot.place(x=str(w+2*s2)+'c', y=str(d+2*h+4*s)+'c', width=str(w)+'c', height=str(h)+'c')
	bSquare = Button(frame, bg='black', command=fSquare, fg='#ffffff', text='x^2')
	bSquare.place(x=str(2*w+3*s2)+'c', y=str(d+2*h+4*s)+'c', width=str(w)+'c', height=str(h)+'c')
	bPower = Button(frame, bg='black', command=fPower, fg='#ffffff', text='x^'+chr(9633))
	bPower.place(x=str(3*w+4*s2)+'c', y=str(d+2*h+4*s)+'c', width=str(w)+'c', height=str(h)+'c')
	bLog10 = Button(frame, bg='black', command=fLog10, fg='#ffffff', text='log_10')
	bLog10.place(x=str(4*w+5*s2)+'c', y=str(d+2*h+4*s)+'c', width=str(w)+'c', height=str(h)+'c')
	bLogE = Button(frame, bg='black', command=fLogE, fg='#ffffff', text='ln')
	bLogE.place(x=str(5*w+6*s2)+'c', y=str(d+2*h+4*s)+'c', width=str(w)+'c', height=str(h)+'c')
	
	bMinus = Button(frame, bg='black', command=fMinus, fg='#ffffff', text='(-)')
	bMinus.place(x=str(s2)+'c', y=str(d+3*h+5*s)+'c', width=str(w)+'c', height=str(h)+'c')
	bAngle = Button(frame, bg='black', command=fAngle, fg='#ffffff', text=chr(176)+'\'\"')
	bAngle.place(x=str(w+2*s2)+'c', y=str(d+3*h+5*s)+'c', width=str(w)+'c', height=str(h)+'c')
	bHyp = Button(frame, bg='black', command=fHyp, fg='#ffffff', text='hyp')
	bHyp.place(x=str(2*w+3*s2)+'c', y=str(d+3*h+5*s)+'c', width=str(w)+'c', height=str(h)+'c')
	bSin = Button(frame, bg='black', command=fSin, fg='#ffffff', text='sin')
	bSin.place(x=str(3*w+4*s2)+'c', y=str(d+3*h+5*s)+'c', width=str(w)+'c', height=str(h)+'c')
	bCos = Button(frame, bg='black', command=fCos, fg='#ffffff', text='cos')
	bCos.place(x=str(4*w+5*s2)+'c', y=str(d+3*h+5*s)+'c', width=str(w)+'c', height=str(h)+'c')
	bTan = Button(frame, bg='black', command=fTan, fg='#ffffff', text='tan')
	bTan.place(x=str(5*w+6*s2)+'c', y=str(d+3*h+5*s)+'c', width=str(w)+'c', height=str(h)+'c')
	
	bRCL = Button(frame, bg='black', command=fRCL, fg='#ffffff', text='RCL')
	bRCL.place(x=str(s2)+'c', y=str(d+4*h+6*s)+'c', width=str(w)+'c', height=str(h)+'c')
	bENG = Button(frame, bg='black', command=fENG, fg='#ffffff', text='ENG')
	bENG.place(x=str(w+2*s2)+'c', y=str(d+4*h+6*s)+'c', width=str(w)+'c', height=str(h)+'c')
	bBracketL = Button(frame, bg='black', command=fBracketL, fg='#ffffff', text='(')
	bBracketL.place(x=str(2*w+3*s2)+'c', y=str(d+4*h+6*s)+'c', width=str(w)+'c', height=str(h)+'c')
	bBracketR = Button(frame, bg='black', command=fBracketR, fg='#ffffff', text=')')
	bBracketR.place(x=str(3*w+4*s2)+'c', y=str(d+4*h+6*s)+'c', width=str(w)+'c', height=str(h)+'c')
	bSToD = Button(frame, bg='black', command=fSToD, fg='#ffffff', text='S'+chr(11012)+'D')
	bSToD.place(x=str(4*w+5*s2)+'c', y=str(d+4*h+6*s)+'c', width=str(w)+'c', height=str(h)+'c')
	bMPlus = Button(frame, bg='black', command=fMPlus, fg='#ffffff', text='M+')
	bMPlus.place(x=str(5*w+6*s2)+'c', y=str(d+4*h+6*s)+'c', width=str(w)+'c', height=str(h)+'c')
	
	b7 = Button(frame, bg='#ffffff', command=f7, text='7')
	b7.place(x=str(s1)+'c', y=str(d+5*h+7*s)+'c', width=str(w)+'c', height=str(h)+'c')
	b8 = Button(frame, bg='#ffffff', command=f8, text='8')
	b8.place(x=str(w+2*s1)+'c', y=str(d+5*h+7*s)+'c', width=str(w)+'c', height=str(h)+'c')
	b9 = Button(frame, bg='#ffffff', command=f9, text='9')
	b9.place(x=str(2*w+3*s1)+'c', y=str(d+5*h+7*s)+'c', width=str(w)+'c', height=str(h)+'c')
	bDel = Button(frame, bg='orange', command=fDel, text='Del')
	bDel.place(x=str(3*w+4*s1)+'c', y=str(d+5*h+7*s)+'c', width=str(w)+'c', height=str(h)+'c')
	bAC = Button(frame, bg='orange', command=fAC, text='AC')
	bAC.place(x=str(4*w+5*s1)+'c', y=str(d+5*h+7*s)+'c', width=str(w)+'c', height=str(h)+'c')
	
	b4 = Button(frame, bg='#ffffff', command=f4, text='4')
	b4.place(x=str(s1)+'c', y=str(d+6*h+8*s)+'c', width=str(w)+'c', height=str(h)+'c')
	b5 = Button(frame, bg='#ffffff', command=f5, text='5')
	b5.place(x=str(w+2*s1)+'c', y=str(d+6*h+8*s)+'c', width=str(w)+'c', height=str(h)+'c')
	b6 = Button(frame, bg='#ffffff', command=f6, text='6')
	b6.place(x=str(2*w+3*s1)+'c', y=str(d+6*h+8*s)+'c', width=str(w)+'c', height=str(h)+'c')
	bMul = Button(frame, bg='#ffffff', command=fMul, text=chr(735))
	bMul.place(x=str(3*w+4*s1)+'c', y=str(d+6*h+8*s)+'c', width=str(w)+'c', height=str(h)+'c')
	bDiv = Button(frame, bg='#ffffff', command=fDiv, text=chr(247))
	bDiv.place(x=str(4*w+5*s1)+'c', y=str(d+6*h+8*s)+'c', width=str(w)+'c', height=str(h)+'c')
	
	b1 = Button(frame, bg='#ffffff', command=f1, text='1')
	b1.place(x=str(s1)+'c', y=str(d+7*h+9*s)+'c', width=str(w)+'c', height=str(h)+'c')
	b2 = Button(frame, bg='#ffffff', command=f2, text='2')
	b2.place(x=str(w+2*s1)+'c', y=str(d+7*h+9*s)+'c', width=str(w)+'c', height=str(h)+'c')
	b3 = Button(frame, bg='#ffffff', command=f3, text='3')
	b3.place(x=str(2*w+3*s1)+'c', y=str(d+7*h+9*s)+'c', width=str(w)+'c', height=str(h)+'c')
	bPlus = Button(frame, bg='#ffffff', command=fPlus, text='+')
	bPlus.place(x=str(3*w+4*s1)+'c', y=str(d+7*h+9*s)+'c', width=str(w)+'c', height=str(h)+'c')
	bSub = Button(frame, bg='#ffffff', command=fSub, text='-')
	bSub.place(x=str(4*w+5*s1)+'c', y=str(d+7*h+9*s)+'c', width=str(w)+'c', height=str(h)+'c')
	
	b0 = Button(frame, bg='#ffffff', command=f0,text='0')
	b0.place(x=str(s1)+'c', y=str(d+8*h+10*s)+'c', width=str(w)+'c', height=str(h)+'c')
	bDot = Button(frame, bg='#ffffff', command=fDot, text='.')
	bDot.place(x=str(w+2*s1)+'c', y=str(d+8*h+10*s)+'c', width=str(w)+'c', height=str(h)+'c')
	b10X = Button(frame, bg='#ffffff', command=f10X, text=chr(735)+'10^x')
	b10X.place(x=str(2*w+3*s1)+'c', y=str(d+8*h+10*s)+'c', width=str(w)+'c', height=str(h)+'c')
	bAns = Button(frame, bg='#ffffff', command=fAns, text='Ans')
	bAns.place(x=str(3*w+4*s1)+'c', y=str(d+8*h+10*s)+'c', width=str(w)+'c', height=str(h)+'c')
	bEqual = Button(frame, bg='#ffffff', command=fEqual, text='=')
	bEqual.place(x=str(4*w+5*s1)+'c', y=str(d+8*h+10*s)+'c', width=str(w)+'c', height=str(h)+'c')
	return

#Dimensions
d, w, h, s, s1 = 3, 1.5, 1, 0.5, 0.5
s2 = (6*s1 - w)/7

#Frame details
frame = Tk()
frame.title('Calculator')
frame['width'], frame['height'] = str(5*w + 6*s1)+'c', str(d + 9*h + 11*s)+'c'
frame.resizable(False, False)

#Components used
bShift = bAlpha = bUp = bMode = bOn = bLeft = bRight = bCalc = bInt = bDown = bInverse = bLog = bRatio = bRoot = bSquare = bPower = bLog10 = bLogE = bMinus = bAngle = bHyp = bSin = bCos = bTan = bRCL = bBracketL = bBracketR = bSToD = bMPlus = b7 = b8 = b9 = bDel = bAC = b4 = b5 = b6 = bMul = bDiv = b1 = b2 = b3 = bPlus = bSub = b0 = bDot = b10X = bAns = bEqual = displayFrame = lQue = lAns = None

#Labels
tQue, tAns = StringVar(), StringVar()
op, cur = [], 0

#Memory of calculator
Ans = A = B = C = D = E = F = X = Y = M = 0
ansMode = False

init()
tQue.set('|')
frame.mainloop()