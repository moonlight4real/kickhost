Yellow = '\033[1;33m'
green = '\033[4;32m'
red = '\033[0;31m'
import time
print(''+red)
import os
os.system('clear')
import amino
print("Loading...")
time.sleep(5)
print(""" __  __  ____   ____  _   _ _      _____ _____ _    _ _______
 |  \/  |/ __ \ / __ \| \ | | |    |_   _/ ____| |  | |__   __|
 | \  / | |  | | |  | |  \| | |      | || |  __| |__| |  | |
 | |\/| | |  | | |  | | . ` | |      | || | |_ |  __  |  | |
 | |  | | |__| | |__| | |\  | |____ _| || |__| | |  | |  | |
 |_|  |_|\____/ \____/|_| \_|______|_____\_____|_|  |_|  |_|
""")
a=input("put your email here :")
time.sleep(0.5)
print('\n')
print("MOONLIGHT:great")
time.sleep(0.5)
print('\n')
b=input("put your password here:")
time.sleep(0.5)
print('\n')
print("MOONLIGHT:are you sure?")
time.sleep(0.5)
print('\n')
c=input("put the com id :")
time.sleep(0.5)
print('\n')
print("MOONLIGHT: OK,gimme his user")
time.sleep(0.5)
print('\n')
d=input("put host's user id:")
time.sleep(0.5)
print('\n')
print("MOONLIGHT: thats him?")
time.sleep(0.5)
print('\n')
e=input("put the chat id :")
time.sleep(0.5)
print('\n')
print("MOONLIGHT: CHECKING....")
print('\n')
client = amino.Client()
client.login(email=(a), password=(b))
subclient = amino.SubClient(comId=(c), profile=client.profile)
print("MOONLIGHT: kicking...")
subclient.kick(userId=(d), chatId=(e), allowRejoin=True) #
print('\n\n')
print("MOONLIGHT")
print('\n')
print("MOONLIGHT: uh,sorry, i kick your ass out")
