import os
#################################
W = "\033[1;37m"
R = "\033[1;31m"
G = "\033[1;32m"
Y = "\033[1;33m"
#################################
print ("" + W)
os.system ('echo -n " 𝙳𝙰𝚃𝙴 : "')
os.system('date "+%a %d %b %Y"')
def OPTION():
	print (Y + "【" + G + "1" + Y + "】『" + G + "𝙲𝙻𝙴𝙰𝚁" + Y + "๛" + G + "𝚃𝙴𝚁𝙼𝙸𝙽𝙰𝙻" + Y + "』")
	print (Y + "【" + G + "2" + Y + "】『" + G + "𝙴𝚇𝙸𝚃" + Y + "』")
	print (R + "╭━━━━➤" + Y + "『" + G + "𝙴𝙻𝚂𝙴" + Y + "』")
	print (R + "┣━━━━━➤ " + G + "𝙲𝚃𝚁𝙻 + 𝙲 " + Y + "➤ " + G + "𝙵𝙾𝚁 𝚂𝚃𝙾𝙿")
#################################
def INPUT_FROM_USER():
    USER = input(R + "╰━━━━━━━━➤" + Y + "『" + G + "𝚃𝚈𝙿𝙴" + Y + "๛" + G + "𝚃𝙷𝙴" + Y + "๛" + G + "𝚆𝙾𝚁𝙳" + Y + "』" + G + "==> " + Y)
    if USER == "1":
    	print ("" + W)
    	os.system("clear")
    	os.system ('echo -n " 𝙳𝙰𝚃𝙴 : "')
    	os.system('date "+%a %d %b %Y"')
    elif USER == "2":
    	print ("\n" + R + "【" + G + "✔" + R + "】" + "𝙱𝚈𝙴𝙴 ...\n")
    	exit()
    else:
    	os.system("espeak " + USER)
    	print (G + "【" + Y + "✔" + G + "】" + W + "𝙳𝚘𝚗𝚎. . . \n\n")
#################################
def main():
	OPTION()
	INPUT_FROM_USER()
#################################
while True:
	if __name__ == "__main__":
		main()
#################################
