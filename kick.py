Yellow = '\033[1;33m'
green = '\033[4;32m'
red = '\033[0;31m'
print(''+red)
import os
os.system('clear')
import amino
print(""" __  __  ____   ____  _   _ _      _____ _____ _    _ _______
 |  \/  |/ __ \ / __ \| \ | | |    |_   _/ ____| |  | |__   __|
 | \  / | |  | | |  | |  \| | |      | || |  __| |__| |  | |
 | |\/| | |  | | |  | | . ` | |      | || | |_ |  __  |  | |
 | |  | | |__| | |__| | |\  | |____ _| || |__| | |  | |  | |
 |_|  |_|\____/ \____/|_| \_|______|_____\_____|_|  |_|  |_|
""")
a=input("put your email here :")
print('\n')
print("MOONLIGHT:great")
print('\n')
b=input("put your password here:")
print('\n')
print("MOONLIGHT:are you sure?")
print('\n')
c=input("put the com id :")
print('\n')
print("MOONLIGHT: OK,gimme his user")
print('\n')
d=input("put host's user id:")
print('\n')
print("MOONLIGHT: thats him?")
print('\n')
e=input("put the chat id :")
print('\n')
print("MOONLIGHT: SANYOARA")
print('\n')
client = amino.Client()
client.login(email=(a), password=(b))
subclient = amino.SubClient(comId=(c), profile=client.profile)
subclient.kick(userId=(d), chatId=(e), allowRejoin=True) #
print('\n\n')
print("MOONLIGHT")
print('\n')
print("MOONLIGHT: uh,sorry, i kick your ass out")
