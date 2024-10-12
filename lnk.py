#!/bin/python3

'''
Scan assigned folder and it's subfolder
1. link kicad_sym or lib or dcm to /home/[USER]/.local/share/kicad/[VER]/symbols
2. link subfolder [model_name].pretty to /home/[USER]/.local/share/kicad/[VER]/footprints
3. link subfolder [model_name].3dshapes to /home/[USER]/.local/share/kicad/[VER]/3dmodels
[optional]4. Add upper folders into kicad symbol and footprint

TODO: manully link footprint with 3d model
'''

'''
[usage]
lnk.py -s [src folder] -ov [target version] -op [target path]
'''

from pathlib import Path
import glob
import os, sys
import argparse

class part_info(object):
  def __init__(self):
    self.sym_list = []
    self.part_name = ""
    self.footprint_list = []
    self.threedshapes_list = []

  def setup(self, part_folder):
    if os.path.isdir(part_folder):
      # find all kicad_sym files under this folder
      for sym_path in glob.glob(os.path.join(part_folder, "*.kicad_sym")):
        self.sym_list.append(sym_path)
        self.part_name = Path(sym_path).stem
        footprint_path = os.path.join(part_folder, self.part_name+".pretty")
        if os.path.isdir(footprint_path):
          self.footprint_list.append(footprint_path)
        else:
          print("no footprint found: "+footprint_path)

        threedshapes_path = os.path.join(part_folder, self.part_name+".3dshapes")
        if os.path.isdir(threedshapes_path):
          self.threedshapes_list.append(threedshapes_path)
        else:
          print("no 3dshapes found: "+threedshapes_path)
    if len(self.sym_list) == len(self.footprint_list):
      return True
    return False
  

  def get_partname(self):
    return self.part_name
  
  def get_sym_path(self):
    return self.sym_list

  def get_footprint_path(self):
    return self.footprint_list

  def get_threedshapes_path(self):
    return self.threedshapes_list


if __name__ == "__main__":
  parser = argparse.ArgumentParser(description="link source folder to target kicad version")
  parser.add_argument("-s", "--src-path", type=str, required=True, help="Soruce folder of kicad resources")
  parser.add_argument("-v", "--output-ver", type=str, help="Output kicad version")
  parser.add_argument("-p", "--output-path", type=str, help="Output kicad resource folder")

  args = parser.parse_args()

  if not (args.output_ver or args.output_path):
    print("Error: you must provide -v or -p")
    sys.exit(-1)
  elif (args.output_ver and args.output_path):
    print("Error: you cannot provide both of -v or -p")
    sys.exit(-1)

  print(args.src_path)
  if (args.output_path):
    print(args.output_path)
  if (args.output_ver):
    print(args.output_ver)

  # list all folders under src_path
  part_list = glob.glob(args.src_path+"/*/")
  if len(part_list) == 0:
    print("No folder found in src : " + args.src_path)
    sys.exit(-1)

  print(f"Found {part_list}")

  part_info_list = []

  for part in part_list:
    pi = part_info()
    if (pi.setup(part)):
      print(f"folder = {part} \r\npart name = {pi.get_partname()}, \r\nsymbols: {pi.get_sym_path()}, \r\nfootprint: {pi.get_footprint_path()}, \r\n3dshapes: {pi.get_threedshapes_path()}")
      part_info_list.append(pi)
      print("")
