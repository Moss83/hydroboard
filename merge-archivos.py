
completo = ["Humedad;Precipitacion\n"]
nombre_humedad = "Humedad-Colon.csv"
nombre_precipitacion = "Precipitacion-Colon.csv"
try:
    lectura = open("C:\\Users\\mauri\\OneDrive\\Escritorio\\UADE\\5° Año\\Proyecto Final de Ingeniería Informática\\hydroboard\\M_" + nombre_humedad)
    lectura.readline()
    linea = lectura.readline()
    while linea:
        lista = linea.removesuffix("\n").split(";")
        completo.append(str(lista[1]) + ".1")
        linea = lectura.readline()
except OSError:
    print("Error SO lectura")
finally:
    try:
        lectura.close()
    except NameError:
        pass

try:
    lectura = open("C:\\Users\\mauri\\OneDrive\\Escritorio\\UADE\\5° Año\\Proyecto Final de Ingeniería Informática\\hydroboard\\M_" + nombre_precipitacion)
    lectura.readline()
    linea = lectura.readline()
    i = 1
    while linea:
        lista = linea.removesuffix("\n").split(";")
        if 30 < float(lista[1]) < 120:
            completo[i] = completo[i] + ";" + str(lista[1]) + "\n"
        else:
            completo[i] = ""
        linea = lectura.readline()
        i += 1
except OSError:
    print("Error SO lectura")
finally:
    try:
        lectura.close()
    except NameError:
        pass

try:
    escritura = open("C:\\Users\\mauri\\OneDrive\\Escritorio\\UADE\\5° Año\\Proyecto Final de Ingeniería Informática\\hydroboard\\M_Datos-Colon.csv", "wt")
    escritura.writelines(completo)
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