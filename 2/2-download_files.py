'''
Load function that's:
 - make a request to a url list
 - obtains the content from the request
 - extract zip files
 - filter all files that is not a .csv files and delete the rest
'''

import os
import requests, zipfile, io
import subprocess

dir_name = "../downloads"

def delete_files():
    print("Elimina archivos!!!!")
    for f in os.listdir("../downloads"):
        print(f)
        bashCommand = "rm -rf " + f
        process = subprocess.Popen(bashCommand.split(), stdout=subprocess.PIPE)
        o, _ = process.communicate()
        print(o)
        print("--------")
        print("------------------------------")

def load_csv_to_bq():
    print("Carga de archivos en BQ")
    for f in os.listdir("../downloads"):
        if f.endswith(".csv"):
            print(f)
            bashCommand = "bq load --null_marker=null --skip_leading_rows=1 --source_format=CSV --field_delimiter=; --allow_quoted_newlines=TRUE --allow_jagged_rows=TRUE data_chile.asistencia ../downloads/" + f
            process = subprocess.Popen(bashCommand.split(), stdout=subprocess.PIPE)
            o, _ = process.communicate()
            print(o)
            print("--------")
        print("------------------------------")

def clean_not_csv_files():
    print("------------------------------")
    print("Limpieza de archivos que no corresponden a CSV")

    for item in os.listdir(dir_name):
        if not item.endswith(".csv"):
            os.remove(os.path.join(dir_name, item))

    print("------------------------------")


'''
"https://datosabiertos.mineduc.cl/wp-content/uploads/2021/12/Asistencia-Declarada-Diciembre-2019.zip",
"https://datosabiertos.mineduc.cl/wp-content/uploads/2021/12/Asistencia-Declarada-Noviembre-2019.zip",
"https://datosabiertos.mineduc.cl/wp-content/uploads/2021/12/Asistencia-Declarada-Octubre-2019.zip",
"https://datosabiertos.mineduc.cl/wp-content/uploads/2021/12/Asistencia-Declarada-Septiembre-2019.zip",
"https://datosabiertos.mineduc.cl/wp-content/uploads/2021/12/Asistencia-Declarada-Agosto-2019.zip",
"https://datosabiertos.mineduc.cl/wp-content/uploads/2021/12/Asistencia-Declarada-Julio-2019.zip",
"https://datosabiertos.mineduc.cl/wp-content/uploads/2021/12/Asistencia-Declarada-Junio-2019.zip",
"https://datosabiertos.mineduc.cl/wp-content/uploads/2021/12/Asistencia-Declarada-Mayo-2019.zip",
"https://datosabiertos.mineduc.cl/wp-content/uploads/2021/12/Asistencia-Declarada-abril-2019.zip",
"https://datosabiertos.mineduc.cl/wp-content/uploads/2021/12/Asistencia-Declarada-Marzo-2019.zip",
"https://datosabiertos.mineduc.cl/wp-content/uploads/2022/02/Asistencia-Declarada-Diciembre-2018.rar",
"https://datosabiertos.mineduc.cl/wp-content/uploads/2022/02/Asistencia-Declarada-Noviembre-2018.rar",
"https://datosabiertos.mineduc.cl/wp-content/uploads/2022/02/Asistencia-Declarada-Octubre-2018.rar",
"https://datosabiertos.mineduc.cl/wp-content/uploads/2022/02/Asistencia-Declarada-Septiembre-2018.rar",
"https://datosabiertos.mineduc.cl/wp-content/uploads/2022/02/Asistencia-Declarada-Agosto-2018.rar",
"https://datosabiertos.mineduc.cl/wp-content/uploads/2022/02/Asistencia-Declarada-Julio-2018.rar",
"https://datosabiertos.mineduc.cl/wp-content/uploads/2022/02/Asistencia-Declarada-Junio-2018.rar",
"https://datosabiertos.mineduc.cl/wp-content/uploads/2022/02/Asistencia-Declarada-Mayo-2018.rar",
"https://datosabiertos.mineduc.cl/wp-content/uploads/2022/02/Asistencia-Declarada-Abril-2018.rar",
"https://datosabiertos.mineduc.cl/wp-content/uploads/2022/02/Asistencia-Declarada-Marzo-2018.rar",
"https://datosabiertos.mineduc.cl/wp-content/uploads/2022/02/Asistencia-Declarada-Diciembre-2017.zip",
"https://datosabiertos.mineduc.cl/wp-content/uploads/2022/02/Asistecia-Declarada-Noviembre-2017.zip",
"https://datosabiertos.mineduc.cl/wp-content/uploads/2022/02/Asistencia-Declarada-Octubre-2017.zip",
"https://datosabiertos.mineduc.cl/wp-content/uploads/2022/02/Asistencia-Declarada-Septiembre-2017.zip",
"https://datosabiertos.mineduc.cl/wp-content/uploads/2022/02/Asistencia-Declarada-Agosto-2017.zip",
"https://datosabiertos.mineduc.cl/wp-content/uploads/2022/02/Asistencia-Declarada-Julio-2017.zip",
"https://datosabiertos.mineduc.cl/wp-content/uploads/2022/02/Asistencia-Declarada-Junio-2017.zip",
"https://datosabiertos.mineduc.cl/wp-content/uploads/2022/02/Asistencia-Declarada-Mayo-2017.zip",
"https://datosabiertos.mineduc.cl/wp-content/uploads/2022/02/Asistencia-Declarada-Abril-2017.zip",
"https://datosabiertos.mineduc.cl/wp-content/uploads/2022/02/Asistencia-Declarada-Marzo-2017.zip",
"https://datosabiertos.mineduc.cl/wp-content/uploads/2021/12/Asistencia-decalarada-diciembre-2016.zip",
"https://datosabiertos.mineduc.cl/wp-content/uploads/2021/12/Asistencia-declarada-noviembre-2016.zip",
"https://datosabiertos.mineduc.cl/wp-content/uploads/2021/12/Asistencia-declarada-octubre-2016.zip",
"https://datosabiertos.mineduc.cl/wp-content/uploads/2021/12/Asistencia-declarada-septiembre-2016.zip",
"https://datosabiertos.mineduc.cl/wp-content/uploads/2021/12/Asistencia-Declarada-Julio-2016.zip",
"https://datosabiertos.mineduc.cl/wp-content/uploads/2021/12/Asistencia-Declarada-Junio-2016.zip",
"https://datosabiertos.mineduc.cl/wp-content/uploads/2021/12/Asistencia-Declarada-Mayo-2016.zip",
"https://datosabiertos.mineduc.cl/wp-content/uploads/2021/12/Asistencia-Declarada-Marzo-2016.zip",
"https://datosabiertos.mineduc.cl/wp-content/uploads/2021/12/Asistencia-declarada-agosto-2016.zip",
"https://datosabiertos.mineduc.cl/wp-content/uploads/2021/12/Asistencia-Declarada-Abril-2016.zip",
"https://datosabiertos.mineduc.cl/wp-content/uploads/2021/12/Asistencia-declarada-diciembre-2015.zip",
"https://datosabiertos.mineduc.cl/wp-content/uploads/2021/12/Asistencia-Declarada-noviembre-2015.zip",
"https://datosabiertos.mineduc.cl/wp-content/uploads/2021/12/Asistencia-Declarada-octubre-2015.zip",
"https://datosabiertos.mineduc.cl/wp-content/uploads/2021/12/Asistencia-Declarada-septiembre-2015.zip",
"https://datosabiertos.mineduc.cl/wp-content/uploads/2021/12/Asistencia-Declarada-agosto-2015.zip",
"https://datosabiertos.mineduc.cl/wp-content/uploads/2021/12/Asistencia-Declarada-julio-2015.zip",
"https://datosabiertos.mineduc.cl/wp-content/uploads/2021/12/Asistencia-Declarada-junio-2015.zip",
"https://datosabiertos.mineduc.cl/wp-content/uploads/2021/12/Asistencia-Declarada-mayo-2015.zip",
"https://datosabiertos.mineduc.cl/wp-content/uploads/2021/12/Asistencia-Declarada-abril-2015.zip",
"https://datosabiertos.mineduc.cl/wp-content/uploads/2021/12/Asistencia-Declarada-marzo-2015.zip"
'''

l = [
    "https://datosabiertos.mineduc.cl/wp-content/uploads/2021/12/Asistencia-Declarada-Diciembre-2019.zip",
    "https://datosabiertos.mineduc.cl/wp-content/uploads/2021/12/Asistencia-Declarada-Noviembre-2019.zip",
    "https://datosabiertos.mineduc.cl/wp-content/uploads/2021/12/Asistencia-Declarada-Octubre-2019.zip",
    "https://datosabiertos.mineduc.cl/wp-content/uploads/2021/12/Asistencia-Declarada-Septiembre-2019.zip",
    "https://datosabiertos.mineduc.cl/wp-content/uploads/2021/12/Asistencia-Declarada-Agosto-2019.zip",
    "https://datosabiertos.mineduc.cl/wp-content/uploads/2021/12/Asistencia-Declarada-Julio-2019.zip",
    "https://datosabiertos.mineduc.cl/wp-content/uploads/2021/12/Asistencia-Declarada-Junio-2019.zip",
    "https://datosabiertos.mineduc.cl/wp-content/uploads/2021/12/Asistencia-Declarada-Mayo-2019.zip",
    "https://datosabiertos.mineduc.cl/wp-content/uploads/2021/12/Asistencia-Declarada-abril-2019.zip",
    "https://datosabiertos.mineduc.cl/wp-content/uploads/2021/12/Asistencia-Declarada-Marzo-2019.zip",
]

os.makedirs(dir_name, exist_ok=True)
print("Descarga de archivos")
for i in l:
    r = requests.get(i)
    z = zipfile.ZipFile(io.BytesIO(r.content))
    z.extractall(dir_name)
    z.close()
    print(i)

    clean_not_csv_files()
    load_csv_to_bq()
    delete_files()

    print("######################################################################")



