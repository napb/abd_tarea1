import subprocess
import os

for f in os.listdir():
    if f.endswith(".csv"):
        print(f)
        bashCommand = "bq load --null_marker=null --skip_leading_rows=1 --source_format=CSV --field_delimiter=; --allow_quoted_newlines=TRUE --allow_jagged_rows=TRUE data_chile.asistencia ./" + f
        process = subprocess.Popen(bashCommand.split(), stdout=subprocess.PIPE)
        o, _ = process.communicate()
        print(o)