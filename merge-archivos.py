
completo = ["DIA;TEMP;H.R.;VIENTO;PREC;FFMC;DMC;DC\n"]

año = 2008

while año < 2024:
    nombre_archivo = "El Palmar " + str(año) + ".csv"

    try:
        lectura = open("C:\\Users\\mauri\\OneDrive\\Escritorio\\UADE\\5° Año\\Proyecto Final de Ingeniería Informática\\hydroboard\\Data\\M_" + nombre_archivo)
        lectura.readline()
        linea = lectura.readline()
        while linea:
            lista = linea.removesuffix("\n").split(";")
            lista[0] = str(lista[0]) + "-" + str(nombre_archivo[10:14])
            unir = ";".join(lista) + "\n"
            completo.append(unir)
            linea = lectura.readline()
    except OSError:
        print("Error SO lectura")
    finally:
        try:
            lectura.close()
        except NameError:
            pass

    año += 1


try:
    escritura = open("C:\\Users\\mauri\\OneDrive\\Escritorio\\UADE\\5° Año\\Proyecto Final de Ingeniería Informática\\hydroboard\\Data\\M_El Palmar.csv", "wt")
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