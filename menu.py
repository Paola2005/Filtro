import citas 
if __name__ == '__main__':
    opc=0 
    peligro=True
    datacitas={"data":[]}
while peligro:
    print(":::CampusMd:::")
    print("Menu Principal")
    opc=int(input("Ingrese una opcion: \n1.citas\n2.Salir \n="))
    if (opc==1):
        citas.LoadInfocitas ()
        citas.menu()
    elif (opc==2):
        print("Byee")
        break
    else:
        print("opcion invalida")
        peligro=False
