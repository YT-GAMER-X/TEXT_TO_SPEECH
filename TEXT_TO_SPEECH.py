import os
#################################
W = "\033[1;37m"
R = "\033[1;31m"
G = "\033[1;32m"
Y = "\033[1;33m"
#################################
print ("" + W)
os.system ('echo -n " π³π°ππ΄ : "')
os.system('date "+%a %d %b %Y"')
def OPTION():
	print (Y + "γ" + G + "1" + Y + "γγ" + G + "π²π»π΄π°π" + Y + "ΰΉ" + G + "ππ΄ππΌπΈπ½π°π»" + Y + "γ")
	print (Y + "γ" + G + "2" + Y + "γγ" + G + "π΄ππΈπ" + Y + "γ")
	print (R + "β­βββββ€" + Y + "γ" + G + "π΄π»ππ΄" + Y + "γ")
	print (R + "β£ββββββ€ " + G + "π²πππ» + π² " + Y + "β€ " + G + "π΅πΎπ πππΎπΏ")
#################################
def INPUT_FROM_USER():
    USER = input(R + "β°βββββββββ€" + Y + "γ" + G + "πππΏπ΄" + Y + "ΰΉ" + G + "ππ·π΄" + Y + "ΰΉ" + G + "ππΎππ³" + Y + "γ" + G + "==> " + Y)
    if USER == "1":
    	print ("" + W)
    	os.system("clear")
    	os.system ('echo -n " π³π°ππ΄ : "')
    	os.system('date "+%a %d %b %Y"')
    elif USER == "2":
    	print ("\n" + R + "γ" + G + "β" + R + "γ" + "π±ππ΄π΄ ...\n")
    	exit()
    else:
    	os.system("espeak " + USER)
    	print (G + "γ" + Y + "β" + G + "γ" + W + "π³πππ. . . \n\n")
#################################
def main():
	OPTION()
	INPUT_FROM_USER()
#################################
while True:
	if __name__ == "__main__":
		main()
#################################
