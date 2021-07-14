def impuestos_sin_coparticipacion():
    datos=open("datos.csv","r")
    impuestos={}
    for i in range (24):
        linea=datos.readline()
        lista=linea.split(",")
        impuestos[lista[0]]=[int(lista[1]),int(lista[2]),int(lista[3]),int(lista[4]),int(lista[5])]
    datos.close()
    return impuestos
def impuestos_coparticipacion():
    imp_cop={}
    datos=open("datos.csv","r")
    for i in range (24):
        linea=datos.readline()
        linea=linea.rstrip()
        lista=linea.split(",")
        imp_cop[lista[0]]=[int(lista[1])+int(lista[2])+int(lista[3])+int(lista[4])+int(lista[5]),int(lista[6])]
    datos.close()
    return imp_cop
def impuesto_maximo (impuestos):
    print("{:-^90}".format("IMPUESTO MAXIMO ABONADO: "))
    print("\n{:<20} {:^39} {:^35}".format("Provincia:","Monto en millones de pesos:","Tipo de impuesto:\n"))
    for provincia in impuestos:
        mayor_impuesto=0
        contador=0
        for elemento in impuestos[provincia]:
            contador+=1
            if (elemento>mayor_impuesto):
                mayor_impuesto=elemento
                if (contador==1):
                    imp="IVA"
                elif (contador==2):
                    imp="Ganancias"
                elif (contador==3):
                    imp="Contribuciones"
                elif (contador==4):
                    imp="Exportaciones"
                elif (contador==5):
                    imp="otros"  
        print("{:<30} {:>10} {:^70}".format(provincia, mayor_impuesto, imp))    
def suma_impuestos_anual (impuestos):
    iva=0
    ganancias=0
    contribuciones=0
    exportaciones=0
    otros=0
    for provincia in impuestos:
        contador=0
        for elemento in impuestos[provincia]:
            contador+=1
            if (contador==1):
                iva+=elemento
            if (contador==2):
                ganancias+=elemento
            if (contador==3):
                contribuciones+=elemento
            if (contador==4):
                exportaciones+=elemento
            if (contador==5):
                otros+=elemento
    print("\n{:-^90}".format("TOTAL ANUAL DE IMPUESTOS: "))
    print("\n{:>17} {:>6} {:<20}".format("IVA:",iva,"MILLONES DE PESOS"))
    print("{:>17} {:>6} {:<20}".format("GANANCIAS:",ganancias,"MILLONES DE PESOS"))
    print("{:>17} {:>6} {:<20}".format("CONTRIBUCIONES:",contribuciones,"MILLONES DE PESOS"))
    print("{:>17} {:>6} {:<20}".format("EXPORTACIONES:",exportaciones,"MILLONES DE PESOS"))
    print("{:>17} {:>6} {:<20}".format("OTROS:",otros,"MILLONES DE PESOS"))
    if (iva>ganancias) and (iva>contribuciones) and (iva>exportaciones) and (iva>otros):
        print("\nEL IVA FUE EL MAYOR IMPUESTO ABONADO: ",iva,"MILLONES DE PESOS")
    else:
        print("EL IVA NO FUE EL MAYOR IMPUESTO ABONADO")
def retribucion(imp_cop):
    print("\n{:-^90}".format("PORCENTAJE DE RETRIBUCION POR PROVINCIA: "))
    print()
    for provincia in imp_cop:
        aporte=0
        contador=0
        for elemento in imp_cop[provincia]:
            contador+=1
            if (contador==1):
                aporte=elemento
            if (contador==2):
                print("{:>19} {:>3} {:<1}".format(provincia,((elemento*100)//aporte),"%"))
def main ():
    impuestos=impuestos_sin_coparticipacion()
    imp_cop=impuestos_coparticipacion()
    impuesto_maximo(impuestos)
    suma_impuestos_anual (impuestos)
    retribucion(imp_cop)
main()
