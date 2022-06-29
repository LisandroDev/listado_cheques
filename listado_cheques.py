import csv
import sys
from datetime import date , datetime
from pprint import pprint


cheques = [];
estados = ["PENDIENTE","APROBADO","RECHAZADO"];

def filtradoPorFecha(rango):
    argumento_fecha = rango.split(":")
    fechaUno = list(map(int,argumento_fecha[0].split("-")));
    fechaDos = list(map(int,argumento_fecha[1].split("-")));
    fechaDesde = date(fechaUno[2],fechaUno[1],fechaUno[0]);
    fechaHasta = date(fechaDos[2],fechaDos[1],fechaDos[0]);
    for cheque in cheques[:]:
        if date.fromtimestamp(int(cheque["FechaPago"])) > fechaHasta or date.fromtimestamp(int(cheque["FechaOrigen"])) < fechaDesde:
            cheques.remove(cheque);

def salida(tipo):
    if tipo.upper() == "PANTALLA":
        for cheque in cheques:
            pprint(cheque)
            print("\n")
    else:
        dt = datetime.now()
        with open(f'{sys.argv[2]}_{int(round(datetime.timestamp(dt)))}','w') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames= ['NroCheque','FechaOrigen', 'FechaPago', 'NumeroCuentaDestino', 'NumeroCuentaOrigen', 'Valor'], extrasaction='ignore')
            writer.writeheader()
            writer.writerows(cheques)


# Lee y crea dictionario con el csv
CSV_FILE = open(sys.argv[1], "r")
csv_dict = csv.DictReader(CSV_FILE);



# Filtra cheques del CSV que contengan el DNI especifico

for cheque in csv_dict:
    if cheque["DNI"] == sys.argv[2]:
        cheques.append(cheque);

CSV_FILE.close();

# Elimina los cheques del array que no sean del Tipo especificado

for cheque in cheques[:]:
    if cheque["Tipo"] != sys.argv[4].upper():
        cheques.remove(cheque)

# Verifica existencia de argumentos opcionales

if len(sys.argv) > 5:
    if sys.argv[5].upper() in estados:
        for cheque in cheques[:]:
            if cheque["Estado"] != sys.argv[5].upper():
                cheques.remove(cheque)
    else:
        filtradoPorFecha(sys.argv[5])
    if len(sys.argv) > 6:
        filtradoPorFecha(sys.argv[6])


salida(sys.argv[3])
    
        