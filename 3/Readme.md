1-  ejecuta en BQ para añadir nuevas columnas LAT, LONG
``` bigquery
ALTER TABLE `infinite-lens-352300.data_chile.asistencia` ADD COLUMN LAT_COMUNA STRING;
ALTER TABLE `infinite-lens-352300.data_chile.asistencia` ADD COLUMN LONG_COMUNA STRING;
```

2- ejecuta ```3-load-comunas-file.py```

3- ejecuta en BQ para modificar tabla asistencia la latitud y longitud
``` bigquery
UPDATE `infinite-lens-352300.data_chile.asistencia` a SET
  a.LAT_COMUNA = b.LATTITUD,
  a.LONG_COMUNA = b.LONGITUD
FROM 
  `infinite-lens-352300.data_chile.info_comunas` b
WHERE 
  a.NOM_COM_RBD = UPPER(b.NOMBRE)
AND 
  a.RBD IS NOT NULL
```
deben ser 354 registros
``` bigquery
SELECT NOM_COM_RBD,LAT_COMUNA,LONG_COMUNA  FROM `infinite-lens-352300.data_chile.asistencia`
WHERE 
  RBD IS NOT NULL
GROUP BY
  NOM_COM_RBD,
  LAT_COMUNA,
  LONG_COMUNA
```

