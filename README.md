# ImportandCopyLocation
This Script is done for Win, for any POSIX System the Directories will be called differently

This script iterates through a given dir and looks for the newest version of an OBJ File, imports it and applies a "copy Location" constraint

The Directory itself dosent matter, the String looks for the last few Chars in its String. Naming convention is "V"/"v" for "Version" and then a Integer from 1-99.
Going over a hundred would require a new IF Statement for the last few characters.

Also the "copylocation" Method needs an already existing objectname of an Object to apply the new constrain


![image](https://github.com/PaulPiper96/ImportandCopyLocation/assets/62021741/1d8d120e-48a5-4637-8c07-ab5a3297c525)



@startuml
start

while (check filesize ?) is (not empty)
  :read file;
endwhile (return iteration)
:append model name;

while (check dir string) is (!= wrong symbol)
  :replace symbol;
endwhile (return blender readble directory)
:return correct blender dir;

:import newest Iteration;

:get Object to copy Location;

:apply object location to new Model;

stop
@enduml
