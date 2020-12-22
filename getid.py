Yellow = '\033[1;33m'
green = '\033[4;32m'
red = '\033[0;31m'
import amino
import time
import os
print(''+red)
print("""__  __  ____   ____  _   _ _      _____ _____ _    _ _______
 |  \/  |/ __ \ / __ \| \ | | |    |_   _/ ____| |  | |__   __|
 | \  / | |  | | |  | |  \| | |      | || |  __| |__| |  | |
 | |\/| | |  | | |  | | . ` | |      | || | |_ |  __  |  | |
 | |  | | |__| | |__| | |\  | |____ _| || |__| | |  | |  | |
 |_|  |_|\____/ \____/|_| \_|______|_____\_____|_|  |_|  |_|""")
print('\n')
print('\n')
print('\n')
print("MOONLIGHT: oh, hi")
time.sleep(0.5)
print('\n')
a=input("put your email here :")
time.sleep(0.5)
print('\n')
print("great!")
time.sleep(0.5)
print('\n')
b=input("put your password here :")
time.sleep(0.5)
print('\n')
print("are you sure? great now gimme the link")
time.sleep(0.5)
print('\n')
c=input("put the link :")
time.sleep(0.5)
print('\n')
print('\n')
client = amino.Client()
email = (a)
password = (b)
print("CHECKING...")
time.sleep(5)
client.login(email=email, password=password)
print("email ✅")
time.sleep(2)
print("password ✅")
time.sleep(2)
print("checking link...")
time.sleep(2)
id = client.get_from_code(c).objectId
print("link ✅")
time.sleep(2)
print("getting...")
time.sleep(3)
print(id)