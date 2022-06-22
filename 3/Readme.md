1- Añade nuevas columnas LAT, LONG

``` bigquery
ALTER TABLE `infinite-lens-352300.data_chile.asistencia` ADD COLUMN LAT_COMUNA STRING;
ALTER TABLE `infinite-lens-352300.data_chile.asistencia` ADD COLUMN LONG_COMUNA STRING;
```