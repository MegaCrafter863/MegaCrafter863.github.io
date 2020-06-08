import pfont
import time
import os

def clears ():
	print(chr(27) + "[2J")

def sc (h, scp):
	k = h[scp:len(h)]
	c = k + h[0:scp]
	h = c
	return h


def scrolltext (inputkk, scp, scl):
	count = 0
	lentt = len(inputkk)

	global okk1
	global okk2
	global okk3
	global okk4
	global okk5
	global okk6
	global okk7

	okk1 = ""
	okk2 = ""
	okk3 = ""
	okk4 = ""
	okk5 = ""
	okk6 = ""
	okk7 = ""

	while(True):
		if(count==lentt):
			break

		Inputf = pfont.getfont(inputkk[count])
		lf = len(Inputf)
		mf1 = round(lf / 7)
		mf2 = 0
		kf1 = mf2
		mf2 = mf2 + mf1
		kf2 = mf2
		mf2 = mf2 + mf1
		kf3 = mf2
		mf2 = mf2 + mf1
		kf4 = mf2
		mf2 = mf2 + mf1
		kf5 = mf2
		mf2 = mf2 + mf1
		kf6 = mf2
		mf2 = mf2 + mf1
		kf7 = mf2
		mf2 = mf2 + mf1
		kf8 = mf2

		okk1 = okk1 + Inputf[kf1:kf2] + "  "
		okk2 = okk2 + Inputf[kf2:kf3] + "  "
		okk3 = okk3 + Inputf[kf3:kf4] + "  "
		okk4 = okk4 + Inputf[kf4:kf5] + "  "
		okk5 = okk5 + Inputf[kf5:kf6] + "  "
		okk6 = okk6 + Inputf[kf6:kf7] + "  "
		okk7 = okk7 + Inputf[kf7:kf8] + "  "

		count = count + 1

	space = ""
	lenk = scl
	count2 = 0
	while(True):
		if(count2>=lenk):
			break
		space = space + " "
		count2 = count2 + 1

	okk1 = okk1 + space
	okk2 = okk2 + space
	okk3 = okk3 + space
	okk4 = okk4 + space
	okk5 = okk5 + space
	okk6 = okk6 + space
	okk7 = okk7 + space

	while(True):
		clears()
		print(okk1[0:scl])
		print(okk2[0:scl])
		print(okk3[0:scl])
		print(okk4[0:scl])
		print(okk5[0:scl])
		print(okk6[0:scl])
		print(okk7[0:scl])

		okk1 = sc(okk1, scp)
		okk2 = sc(okk2, scp)
		okk3 = sc(okk3, scp)
		okk4 = sc(okk4, scp)
		okk5 = sc(okk5, scp)
		okk6 = sc(okk6, scp)
		okk7 = sc(okk7, scp)

		time.sleep(0.05)
