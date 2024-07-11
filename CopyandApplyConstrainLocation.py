import os
import bpy


def is_integer(s):
    try:
        int(s)
        return True
    except ValueError:
        return False
    
def casttonum(string):
    if(is_integer(string)):
        return (int(string))
    
def import_model(modeldir, dir, modelname):  
    print(modeldir)
    print(dir)
    print(modelname)
    bpy.ops.wm.obj_import(filepath=modeldir, directory=dir, files=[{"name":modelname, "name":modelname}])
     
  


#get the model name to append to the dir string
def get_model_name(dir):
     file=""
     for root, dirs, files in os.walk(dir):
        for _file in files:
            if(_file[len(_file)-3:len(_file)]=="obj"):
                file=_file
     return file


def replace_wrongslashes(paths):
 string=""
 for char in paths:
      if(char=="\\"):
          char='\\'
      if(char=="/"):
          char='\\'
      string+=char
 return string
         
    
#iterate over all folders and find the newest version
def iterate_folders(directory):
 folder=""
 highnum=0
 aktuellenum=0
 for root, dirs, files in os.walk(directory):
        for dir_name in dirs:
            folder_path = os.path.join(root, dir_name)
            if(folder_path[len(folder_path)-2:len(folder_path)-1]=="v" or folder_path[len(folder_path)-2:len(folder_path)-1]=="V"):
                if(is_integer(folder_path[len(folder_path)-1:len(folder_path)])):
                 aktuellenum=casttonum(folder_path[len(folder_path)-1:len(folder_path)])
                 if(aktuellenum>=highnum):
                     highnum=aktuellenum
                     folder=folder_path
            #print(folder_path[len(folder_path)-1:len(folder_path)])
            if(is_integer(folder_path[len(folder_path)-2:len(folder_path)])):
                aktuellenum=casttonum(folder_path[len(folder_path)-2:len(folder_path)])
                if(aktuellenum>=highnum):
                     highnum=aktuellenum
                     folder=folder_path
            else:
                print("NAN")
            
 print("Numbers",folder)
                
 return folder

def constraintlocation(_target):
    head = bpy.context.view_layer.objects[-1]
    cube = bpy.data.objects[_target]
    constraint = head.constraints.new(type='COPY_LOCATION')
    constraint.target =cube


def copylocation(constrainlocation):
    # Select the object by name
    bpy.context.view_layer.objects.active =  bpy.context.view_layer.objects[-1].name
    constraint = bpy.context.object.constraints.new(type='COPY_LOCATION')
    constraint.target = bpy.data.objects[constrainlocation]
   
if __name__ == "__main__":
    dir="" #THIS IS THE LOCATION DIRECTORY TO RUN OVER
    dir=iterate_folders(dir)
    modelname=get_model_name(dir)
    fixmodelstring=replace_wrongslashes(dir +"/" + modelname)
    fixeddir=replace_wrongslashes(dir)
    import_model(fixmodelstring, fixeddir+ "//", modelname)
    print(fixeddir+"\\")
    print(fixmodelstring)
    print(modelname)
    
    constraintlocation("Cube")



   

