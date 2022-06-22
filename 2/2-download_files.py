'''
Load function that's:
 - make a request to a url list
 - obtains the content from the request
 - extract zip files
 - filter all files that is not a .csv files and delete the rest
'''

import os
import requests, zipfile, io

dir_name = "../downloads"

l = [
    "https://datosabiertos.mineduc.cl/wp-content/uploads/2021/12/Asistencia-Declarada-Diciembre-2019.zip",
    "https://datosabiertos.mineduc.cl/wp-content/uploads/2021/12/Asistencia-Declarada-Noviembre-2019.zip",
    "https://datosabiertos.mineduc.cl/wp-content/uploads/2021/12/Asistencia-Declarada-Octubre-2019.zip",
]

os.makedirs(dir_name, exist_ok=True)

for i in l:
    r = requests.get(i)
    z = zipfile.ZipFile(io.BytesIO(r.content))
    z.extractall(dir_name)
    z.close()
    print(i)


test = os.listdir(dir_name)

for item in test:
    if not item.endswith(".csv"):
        os.remove(os.path.join(dir_name, item))