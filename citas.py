import core 
dicccitas={"data":[]}
def LoadInfocitas():
    global dicccitas
    if(core.checkFile("citas.json")):
        dicccitas=core.LoadInfo("citas.json")
    else:
        core.crearinfo("citas.json", dicccitas)
        
def menu():
    peligro=True
    print(":::-Citas-:::")
    print("1. Registrar citas")
    print("2. Consultar citas")
    print("3. Modificar cita")
    print("4. Eliminar cita")
    print("5. Volver menu principal")
    opcion=int(input("Ingrese una opcion: "))
    if (opcion==1):
        print(":::Registrar cita:::")
        print("")
        id=input("Ingrese el id de la cita:")
        while id == ["id"]:
            print("El id ya se encuentra")
            id=input("Ingrese un nuevo id:")
        dia=int(input("Ingrese el dia de la cita:"))
        while (dia<1)or (dia>31):
            print("Ese dia no existe")
            dia=int(input("Ingrese un dia valido: "))
            
        mes=int(input("Ingrese el mes de la cita:"))
        while (mes<1)or (mes>12):
            print("Ese mes no existe")
            mes=int(input("Ingrese un mes valido: "))
            
        año=(input("Ingrese el año de la cita:"))
        while ((len(año)>4)or ((len(año)<4))):
            print("Ese año no existe")
            año=input("Ingrese un año valido:")
        fecha=f'{dia}'+'/'+ f'{mes}'+'/'+ f'{año}'
        
        while True:
            hora=input("Ingrese la hora de la cita HH:MM:")
            h=hora.split(":")
            if len(h)!=2:
                print("La hora es invalida")
                continue
            try:
                horas=int(h[0])
                minutos=int(h[1])
                if 0<=horas<=23 and 0<=minutos <=59:
                    break
                else:
                    print("La hora ingresada es invalida. intente otra vez")
            except ValueError:
        
                print("El formato de hora es incorrecto")   
        print("La hora ingresada es valida:",hora)
        
        
        data={
            "id":id,
            "nombre":input("Ingrese el nombre del paciente:"),
            "fecha":fecha,
            "hora":hora,
            "motivo":input("Ingrese el motivo de la consulta:")
        }
        dicccitas["data"].append (data)
        core.crearinfo("citas.json", data)
        print("Cita registrada")
        input("")

    elif (opcion==2):
        print(":::Consultar citas:::")
        print("1.Buscar por nombre")
        print("2.Buscar por fecha")
        opc=int(input(":"))
        if (opc==1):
            contador=0
            nombre=input("Ingrese el nombre del paciente:")
            for i, item in enumerate(dicccitas["data"]):
                contador+=1
                if nombre==item["nombre"]:
                    print("El paciente se encuentra")
                    print(f"id:{item['id']}\nNombre del paciente:{item['nombre']}\nFecha de la cita{item['fecha']}\nHora de la cita:{item['hora']}\nMotivo de la cita:{item['motivo']}")
                elif (contador==len(dicccitas["data"])):
                    print("El paciente no se encuentra")
        elif (opc==2):
            buscador=input("Ingrese la fecha de la cita a buscar")
            for i, item in enumerate(dicccitas["data"]):
                if buscador in item["fecha"]:
                    print(f'Id cita: {item["id"]}')
                    print(f'Nombre paciente: {item["nombre"]}')
                    print(f'Fecha : {item["fecha"].upper()}')
                    print(f'Hora: {item["hora"]}')
                    print(f'Motivo: {item["motivo"]}')
                else:
                    print("El paciente no se encuentra")
        else:
            pass
            
        
    elif (opcion==3):
        print(":::Modificar citas:::")
        M=input("Ingrese el codigo de la cita a modificar:")
        for x,item in enumerate(dicccitas["data"]):
            if M in item ["id"]:
                item["nombre"]=input("Ingrese el nuevo nombre del paciente o presione enter para omitir:")or item["nombre"]
                item["fecha"]=input("Ingrese la nueva fecha de la cita o presione enter para omitir:") or item["fecha"]
                item["hora"]=input("Ingrese la nueva hora de la cita o presione enter para omitir:") or item["hora"]
                item["motivo"]=input("Ingrese el nuevo motivo de la cita o presione enter para omitir:") or item["motivo"]
                core.EditarData("citas.json",dicccitas)
                
    elif (opcion==4):
        print(":::Eliminar citas:::")
        id=input("Ingrese el codigo de la cita a eliminar:")
        for i,item in enumerate(dicccitas["data"]):
            if id in item["id"]:
                dicccitas["data"].pop(i)
            core.EditarData("citas.json",dicccitas)
    
    elif (opcion==5):
        peligro=False
        
    if (peligro):
        menu()
        