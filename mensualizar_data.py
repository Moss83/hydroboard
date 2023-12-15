def mensualizar(registros):
    mensual = []
    counter = 0
    precipitacion = 0
    mesactual = 0
    temperatura = 0
    humedad = 0
    viento = 0
    ffmc = 0
    dmc = 0
    dc = 0
    for registro in registros:
        if registro[0] != "DIA":
            mes = int(str(registro[0])[4:6])
            if mesactual == 0 or mesactual == mes:
                if mesactual == 0:
                    mesactual = mes
                precipitacion += float(str(registro[4]).replace(",", "."))
                temperatura += float(str(registro[1]).replace(",", "."))
                humedad += float(str(registro[2]).replace(",", "."))
                viento += float(str(registro[3]).replace(",", "."))
                ffmc += float(str(registro[5]).replace(",", "."))
                dmc += float(str(registro[6]).replace(",", "."))
                dc += float(str(registro[7]).replace(",", "."))
                counter += 1
            else:
                insertar = str(mesactual) + ";" + str(int(temperatura / counter)) + ";" + str(int(humedad / counter)) + ";" + str(int(viento / counter)) + ";" + str(int(precipitacion)) + ";" + str(int(ffmc / counter)) + ";" + str(int(dmc / counter)) + ";" + str(int(dc / counter)) + "\n"
                mensual.append(insertar)
                mesactual = mes
                precipitacion = float(str(registro[4]).replace(",", "."))
                temperatura = float(str(registro[1]).replace(",", "."))
                humedad = float(str(registro[2]).replace(",", "."))
                viento = float(str(registro[3]).replace(",", "."))
                ffmc = float(str(registro[5]).replace(",", "."))
                dmc = float(str(registro[6]).replace(",", "."))
                dc = float(str(registro[7]).replace(",", "."))
                counter = 1
    insertar = str(mesactual) + ";" + str(int(temperatura / counter)) + ";" + str(int(humedad / counter)) + ";" + str(int(viento / counter)) + ";" + str(int(precipitacion)) + ";" + str(int(ffmc / counter)) + ";" + str(int(dmc / counter)) + ";" + str(int(dc / counter)) + "\n"
    mensual.append(insertar)
    return mensual

completo = []
nombre = "El Palmar 2023.csv"
try:
    lectura = open("C:\\Users\\mauri\\OneDrive\\Escritorio\\UADE\\5° Año\\Proyecto Final de Ingeniería Informática\\hydroboard\\Data\\" + nombre)
    linea = lectura.readline()
    while linea:
        lista = linea.removesuffix("\n").split(";")
        completo.append(lista)
        linea = lectura.readline()
except OSError:
    print("Error SO lectura")
finally:
    try:
        lectura.close()
    except NameError:
        pass

datos = mensualizar(completo)
print(datos)

try:
    escritura = open("C:\\Users\\mauri\\OneDrive\\Escritorio\\UADE\\5° Año\\Proyecto Final de Ingeniería Informática\\hydroboard\\Data\\M_" + nombre, "wt")
    escritura.write("DIA;TEMP;H.R.;INT VIENTO (km/h);PREC;FFMC;DMC;DC\n")
    escritura.writelines(datos)
except OSError:
    print("Error SO escritura")
except:
    print("Error desconocido escritura")
finally:
    try:
        escritura.close()
        print("Terminado")
    except NameError:
        pass
