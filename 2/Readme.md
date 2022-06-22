1- ejecucion de `2-download_files.py`

2- Creacion de tabla asistencia
``` bigquery
DROP TABLE `infinite-lens-352300.data_chile.asistencia`;

CREATE TABLE 
  `infinite-lens-352300.data_chile.asistencia` (
  AGNO INTEGER,
  MES_ESCOLAR INTEGER,
  RBD INTEGER,
  DGV_RBD INTEGER,
  NOM_RBD STRING,
  COD_REG_RBD INTEGER,
  NOM_REG_RBD_A STRING,
  COD_PRO_RBD INTEGER,
  COD_COM_RBD INTEGER,
  NOM_COM_RBD STRING,
  COD_DEPROV_RBD INTEGER,
  NOM_DEPROV_RBD STRING,
  RURAL_RBD INTEGER,
  COD_DEPE INTEGER,
  COD_DEPE2 STRING,
  COD_ENSE INTEGER,
  COD_ENSE2 INTEGER,
  COD_GRADO INTEGER,
  LET_CUR STRING,
  MRUN INTEGER,
  GEN_ALU INTEGER,
  FEC_NAC_ALU STRING,
  COD_COM_ALU INTEGER,
  NOM_COM_ALU STRING,
  DIAS_ASISTIDOS INTEGER,
  DIAS_TRABAJADOS INTEGER,
  ASIS_PROMEDIO INTEGER
)
PARTITION BY  
  RANGE_BUCKET(RBD, GENERATE_ARRAY(0, 100, 10))
OPTIONS(
  require_partition_filter=true
)
```

3- Carga de datos en BQ
``` shell
bq load --null_marker=null --skip_leading_rows=1 --source_format=CSV --field_delimiter=";" --allow_quoted_newlines=TRUE --allow_jagged_rows=TRUE data_chile.asistencia ./down/[file_csv].csv
```



