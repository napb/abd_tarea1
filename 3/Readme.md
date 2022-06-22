1-  ejecuta en BQ para añadir nuevas columnas LAT, LONG
``` bigquery
ALTER TABLE `infinite-lens-352300.data_chile.asistencia` ADD COLUMN LAT_COMUNA STRING;
ALTER TABLE `infinite-lens-352300.data_chile.asistencia` ADD COLUMN LONG_COMUNA STRING;
```

2- ejecuta ```3-load-comunas-file.py```

3- ejecuta en BQ
``` bigquery
UPDATE `infinite-lens-352300.data_chile.asistencia` a SET
  a.LAT_COMUNA = b.LATTITUD
FROM 
  `infinite-lens-352300.data_chile.info_comunas`
WHERE 
  a.NOM_COM_RBD = UPPER(b.NOMBRE)

```