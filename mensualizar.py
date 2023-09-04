
def mensualizarPrecipitacion(registros):
    mensual = []
    precipitacion = 0
    mesactual = 0
    añoactual = 0
    for registro in registros:
        if registro[0] != "Fecha":
            dia, mes, año = registro[0].split("/")
            if mesactual == 0 or (mesactual == mes and añoactual == año):
                if mesactual == 0:
                    mesactual = mes
                    añoactual = año
                precipitacion += float(str(registro[1]).replace(",", "."))
            else:
                insertar = str(mesactual) + "/" + str(añoactual) + ";" + str(precipitacion) + "\n"
                mensual.append(insertar)
                mesactual = mes
                añoactual = año
                precipitacion = float(str(registro[1]).replace(",", "."))
    return mensual

def mensualizarHumedad(registros):
    mensual = []
    humedad = 0
    counter = 0
    mesactual = 0
    añoactual = 0
    for registro in registros:
        if registro[0] != "Fecha":
            dia, mes, año = registro[0].split("/")
            if mesactual == 0 or (mesactual == mes and añoactual == año):
                if mesactual == 0:
                    mesactual = mes
                    añoactual = año
                humedad += float(str(registro[1]).replace(",", "."))
                counter += 1
            else:
                insertar = str(mesactual) + "/" + str(añoactual) + ";" + str(int(humedad / counter)) + "\n"
                mensual.append(insertar)
                mesactual = mes
                añoactual = año
                humedad = float(str(registro[1]).replace(",", "."))
                counter = 1
    return mensual



#Lectura y extraccion de datos
opcion = int(input("Desea mensualizar precipitaciones (0) o humedad (1)? --> "))

completo = []
nombre = ""
if opcion == 0:
    nombre = "Precipitacion-Colon.csv"
else:
    nombre = "Humedad-Colon.csv"
try:
    lectura = open("C:\\Users\\mauri\\OneDrive\\Escritorio\\UADE\\5° Año\\Proyecto Final de Ingeniería Informática\\hydroboard\\" + nombre)
    linea = lectura.readline()
    while linea:
        lista = linea.removesuffix("\n").split(";")
        fechahora = lista[0].split()
        if len(fechahora) > 0:
            fecha = fechahora[0]
            insertar = [fecha, lista[1]]
            completo.append(insertar)
        linea = lectura.readline()
except OSError:
    print("Error SO lectura")
finally:
    try:
        lectura.close()
    except NameError:
        pass

#Mensualizar datos
if opcion == 0:
    datos = mensualizarPrecipitacion(completo)
else:
    datos = mensualizarHumedad(completo)

#Escritura archivo
try:
    escritura = open("C:\\Users\\mauri\\OneDrive\\Escritorio\\UADE\\5° Año\\Proyecto Final de Ingeniería Informática\\hydroboard\\M_" + nombre, "wt")
    if opcion == 0:
        escritura.write("Fecha;Precipitacion\n")
    else:
        escritura.write("Fecha;Humedad\n")
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

