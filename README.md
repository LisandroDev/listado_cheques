# Script de procesamiento CSV de cheques
Realizado para curso del ITBA Full Stack Developer.


# Funcionamiento

el script posee los siguientes 6 argumentos siendo 2 opcionales:

1. Nombre del archivo csv.

2. DNI del cliente donde se filtraran.

3. Salida: PANTALLA o CSV

Si CSV es especificado se generara el archivo CSV con el siguiente nombre: DNI_TIMESTAMP.csv

4. Tipo de cheque: EMITIDO o DEPOSITADO

5. Estado del cheque: PENDIENTE, APROBADO, RECHAZADO. (Opcional)

6. Rango fecha: xx-xx-xxxx:yy-yy-yyyy (Opcional)


### Ejemplo de uso

$ python3 listado_cheques.py NOMBREARCHIVO.csv DNI SALIDA TIPODECHEQUE ESTADO RANGOFECHA

python3 listado_cheques.py test.csv 23665789 csv emitido aprobado 4-4-2021:4-4-2021

python3 listado_cheques.py test.csv 23665789 csv emitido

