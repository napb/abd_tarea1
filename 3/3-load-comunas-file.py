import csv
import requests
import subprocess

url = "https://raw.githubusercontent.com/napb/abd_tarea1/master/3/comunas.csv"
response = requests.get(url)

with open('../out.csv', 'w') as f:
    writer = csv.writer(f)
    for line in response.iter_lines():
        writer.writerow(line.decode('utf-8').split(','))


bashCommand = "bq load --autodetect --source_format=CSV --field_delimiter=, data_chile.info_comunas ../out.csv"
process = subprocess.Popen(bashCommand.split(), stdout=subprocess.PIPE)
o, _ = process.communicate()
print(o)