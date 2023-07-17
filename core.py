import json
def crearinfo(*args):
    if (checkFile(args[0])==False):
        with open('data/'+args[0],"w") as write_file:
            json.dump(args[1],write_file,indent=4)
            write_file.close()
    else:
        with open('data/'+args[0],'r+')as file:
            file_data = json.load(file)
            file_data["data"].append(args[1])
            file.seek(0)
            json.dump (file_data,file,indent=4)
            file.close()
            
def EditarData(*args):
    with open('data/'+args[0],"w") as write_file:
        json.dump(args[1],write_file, indent=4)
        write_file.close()
        
def LoadInfo(fileName):
    if (checkFile(fileName)==True):
        with open('data/'+fileName,"r")as read_file:
            dicc=json.load(read_file)
        return dicc
        
def checkFile(fileName):
    try:
        with open('data/'+fileName,'r')as f:
            return True
    except FileNotFoundError as e:
        print("Error")
        return False
    except IOError as e:
        return False
            